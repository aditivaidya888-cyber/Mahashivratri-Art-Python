# Mahashivratri Artistic Drawing – Python

A Python-based creative graphics project that uses computer vision and Turtle graphics to transform colored image contours into an artistic line drawing.

## Features

- Loads an input image using OpenCV.
- Resizes the image while maintaining its aspect ratio.
- Identifies gold/orange and cyan-colored regions using HSV color masks.
- Detects contours in the selected regions.
- Draws the detected contours using Python Turtle.
- Uses a black background to highlight the colorful lines.

## Technologies Used

- Python 3
- OpenCV
- NumPy
- Turtle Graphics

## Requirements

Install the required packages:

```bash
pip install opencv-python numpy
```

Turtle is generally included with standard Python installations.

## Project Structure

```text
Mahashivratri-Art-Python/
├── mahashivratri_special.py
├── image.png
├── README.md
└── .gitignore
```

**Note:** The input image must be named `image.png` and placed in the project directory, as expected by the current script.

## How to Run

1. Install Python 3.
2. Install OpenCV and NumPy.
3. Place the desired input image in the project folder and name it `image.png`.
4. Open a terminal in the project directory.
5. Run:

```bash
python mahashivratri_special.py
```

The program opens a Turtle graphics window and draws the detected contours.

## Learning Outcomes

- Image loading and resizing with OpenCV.
- HSV color-space filtering.
- Contour detection and processing.
- Coordinate transformation.
- Creative graphics using Turtle.

## Author

Aditi Vaidya
