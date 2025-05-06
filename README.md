# Real-Time Edge Detection Using OpenCV

This project is a Computer Vision task that performs real-time edge detection on a webcam video stream using various gradient-based techniques.

## 🔍 Features

- Real-time webcam stream processing
- Apply different edge detection filters via keyboard input
- Adjustable Gaussian smoothing with `+` and `-` keys

## 🎮 Controls

| Key | Functionality                              |
|-----|--------------------------------------------|
| `o` | Show original webcam frame                 |
| `x` | Apply Sobel gradient in X direction        |
| `y` | Apply Sobel gradient in Y direction        |
| `m` | Show Sobel magnitude (√(Gx² + Gy²))        |
| `s` | Apply Sobel + thresholding (Bonus)         |
| `l` | Apply Laplacian of Gaussian (LoG) filter   |
| `+` | Increase Gaussian blur sigma               |
| `-` | Decrease Gaussian blur sigma               |
| `q` | Quit the program                           |

## 📦 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install requirements:
```bash
pip install opencv-python numpy

