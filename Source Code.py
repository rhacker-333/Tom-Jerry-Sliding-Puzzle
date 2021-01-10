import pygame, sys, os, tkinter as tk
from tkinter import *
from random import shuffle
pygame.init()
# initialise the colors
white=(255,255,255)
black=(0,0,0)
dark_blue=(0, 6, 246)
lemon_yellow=(232, 236, 48)
crimpson=(255,109,133)


# initialising the class
class ImagePuzzle:
    # constructor
    def __init__(self, grid_size, tile_size, margin_size):
        self.grid_size, self.tile_size, self.margin_size = grid_size, tile_size, margin_size
        # specifying the number of tiles
        self.tiles_len = (grid_size[0]*grid_size[1]) - 1
        self.tiles = [(x,y) for x in range(grid_size[0]) for y in range(grid_size[1])]
        # Original image in the form of tiles
        self.tilesOG = [(x,y) for x in range(grid_size[0]) for y in range(grid_size[1])]    
        self.tilespos = {(x,y):(x*(tile_size+margin_size)+margin_size,y*(tile_size+margin_size)+margin_size) for y in range(grid_size[1]) for x in range(grid_size[0])}     
        w,h = grid_size[0]*(tile_size+margin_size)+margin_size, grid_size[1]*(tile_size+margin_size)+margin_size


        # accept the image from the user
        root = Tk()
        root.destroy()
        # load the image accepted, in the program
        pic = pygame.image.load('G:\IMG-20210109-WA0008.jpg')
        # resizing the image to the window size
        pic = pygame.transform.scale(pic, (w,h))


        # putting the tile images in self.images
        self.images = []
        for i in range(self.tiles_len):
            x,y = self.tilespos[self.tiles[i]]
            # dividing the image into tiles
            image = pic.subsurface(x,y,tile_size,tile_size)
            self.images += [image] 

            
        self.temp = self.tiles[:-1]
        shuffle(self.temp)
        self.temp.insert(len(self.temp), self.tiles[-1])
        self.tiles = self.temp


    def getBlank(self): return self.tiles[-1]
    def setBlank(self, pos): self.tiles[-1] = pos
    
    opentile = property(getBlank, setBlank)
    
    def switch(self, tile):
        n = self.tiles.index(tile)
        self.tiles[n], self.opentile = self.opentile, self.tiles[n] # exchanging the places of the empty tile with the clicked tile
        if self.tiles == self.tilesOG: # checking if the game has been solved or not
            print("COMPLETED !!!")
    
    def is_grid(self, tile): 
        return tile[0] >= 0 and tile[0] < self.grid_size[0] and tile[1] >= 0 and tile[1] < self.grid_size[1]
    
    def adjacent(self):
        x,y = self.opentile;
        return (x-1, y), (x+1,y), (x,y-1), (x,y+1)
    
    def update(self, dt):

        # Find the tile on which the mouse is 
        # Switch as long as open tile is adjacent
        
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        
        # Convert mouse position relative to tile position and check in grid
        if mouse[0]:
            tile = mpos[0]//self.tile_size, mpos[1]//self.tile_size
            
            if self.is_grid(tile): 
                if tile in self.adjacent():
                    self.switch(tile)
    # placing the tiled images on the screen
    def draw(self, screen):
        for i in range(self.tiles_len):
            x,y = self.tilespos[self.tiles[i]]
            screen.blit(self.images[i], (x,y))



# designing the main game screen
font = pygame.font.Font('freesansbold.ttf', 16)
text1 = font.render('Keep on clicking the left mouse button on the tile next to the empty space to proceed with the game.', True, crimpson, black)
text2 = font.render('Unsolved picture', True, lemon_yellow, black)
text3 = font.render('Solved picture', True, lemon_yellow, black)
text4 = font.render('Instructions: ', True, crimpson, black)
textRect4 = text4.get_rect()
textRect4.center = (60, 540)
textRect3 = text3.get_rect()
textRect3.center = (750, 490)
textRect2 = text2.get_rect()
textRect2.center = (250, 490)
textRect = text1.get_rect()
textRect.center = (450, 570)


def main():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1' # placing the game window at the centre of the screen
    pygame.display.set_caption("Image Puzzle") # setting the title of the game window
    screen = pygame.display.set_mode((1000,600))# making the game window
    fpsclock = pygame.time.Clock() # setting the control for Frames per second
    program = ImagePuzzle((3,3), 150, 5) # calling the main game class 
    img1 = pygame.image.load('G:\IMG-20210109-WA0008.jpg') # loading the image once again to a separate variable
    img1 = pygame.transform.scale(img1, (500,469))# transforming the size of the image to fit it into the game window

    # game loop
    while True:
        dt = fpsclock.tick() # setting the frames per second to maximum
        
        screen.fill((0,0,0)) # filling the screen with black background
        
        program.draw(screen) # drawing the screen within game loop
        # aesthetics of the game window
        screen.blit(text1, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(img1, (500, 0))
        pygame.draw.line(screen, dark_blue, [485,0], [485, 510], 5)
        pygame.draw.line(screen, dark_blue, [0, 510], [1000, 510], 5)
        pygame.display.flip() # updating the game window

        # the quit game functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        program.update(dt)

if __name__ == '__main__':
    main()
