# Image Sliding Puzzle Game

A classic sliding tile puzzle game made with **Python** and **Pygame**. Rearrange the shuffled image tiles back to the original picture by sliding the tiles into the empty space!

---

## Features

- Play a 3x3 sliding puzzle with any image
- Simply click adjacent tiles to move them
- See a preview of the original image
- Automatic win detection with a completion message

---

## Requirements

- Python 3.7+
- Pygame (`pip install pygame`)

---

## How to Play

1. **Set Up Your Image:**
   - Place your image (preferably square, e.g. `myphoto.jpg`) in a known location.
   - Update the `image_path` variable in the script to point to your image file.

2. **Run the Game:**


3. **Controls:**
- Click a tile next to the empty space to slide it.
- Keep sliding tiles until the original image is restored!
- A "COMPLETED !!!" message is printed in the terminal when you solve the puzzle.

---

## Setup Instructions

1. **Clone this repository**
 ```
 git clone https://github.com/yourusername/image-sliding-puzzle.git
 cd image-sliding-puzzle
 ```

2. **Install requirements**
 ```
 pip install pygame
 ```

3. **Set your image path**  
 Edit `image_puzzle.py` and update this line:
 ```
 image_path = 'your_image.jpg'  # <--- Set this to your image file location
 ```

4. **Run the game**
 ```
 python image_puzzle.py
 ```

---

## Customization

- **Grid Size:**  
Change the grid size in the script, e.g. for a 4x4 puzzle:

- **Image Size:**  
Use high-quality, square images for best results!
- **Image Path:**  
Ensure `image_path` in the script points to your chosen image.

---

## License

MIT License

---

**Enjoy your puzzle!**

