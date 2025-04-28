import cv2
import numpy as np

cap = cv2.VideoCapture(0)
show_webcam = False
sobel_x = False
sobel_y = False
sobel_m = False
log = False
gus = False
sobel_thresh = False
x = 10  # starting sigma value

# Create a black frame (480x640)
black_frame = np.zeros((480, 640, 3), dtype=np.uint8)

while True:

    key = cv2.waitKey(1) & 0xFF

    if key == ord('o'):
        show_webcam = True  
    elif key == ord('x'):
        sobel_x = True
        sobel_y = sobel_m = log = gus = sobel_thresh = False
    elif key == ord('y'):
        sobel_y = True
        sobel_x = sobel_m = log = gus = sobel_thresh = False
    elif key == ord('m'):
        sobel_m = True
        sobel_x = sobel_y = log = gus = sobel_thresh = False
    elif key == ord('l'):
        log = True 
        sobel_x = sobel_y = sobel_m = gus = sobel_thresh = False
    elif key == ord('g'):
        gus = True 
        sobel_x = sobel_y = sobel_m = log = sobel_thresh = False
    elif key == ord('s'):
        sobel_thresh = True   
        sobel_x = sobel_y = sobel_m = log = gus = False
    elif key == ord('+') or key == ord('='):  
        x += 10
    elif key == ord('-'):
        x = max(1, x - 10)  # prevent sigma from being 0 or negative
    elif key == ord('q'):
        break

    if not show_webcam:
        cv2.imshow('Press O to Start Webcam', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_show = frame
        cv2.imshow('Webcam', frame_show)
        if key == ord('e'):
            show_webcam = False
            frame_show = black_frame

    # Calculate dynamic kernel size
    k = int((x / 10) * 2 + 1)
    if k % 2 == 0:
        k += 1

    if not sobel_x:
        cv2.imshow('x', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (k, k), sigmaX=x)
        sobelX = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=5)
        frame_show = sobelX
        cv2.imshow('Sobel X', frame_show)
        if key == ord('e'):
            sobel_x = False

    if not sobel_y:
        cv2.imshow('connect to Y', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (k, k), sigmaX=x)
        sobelY = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)
        frame_show = sobelY
        cv2.imshow('Sobel Y', frame_show)
        if key == ord('e'):
            sobel_y = False

    if not sobel_m:
        cv2.imshow('Connect to Magnitude', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (k, k), sigmaX=x)
        sobelX = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=3)
        sobelY = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)
        mag = cv2.magnitude(sobelX, sobelY).astype(np.uint8)
        frame_show = mag
        cv2.imshow('Magnitude', mag)
        if key == ord('e'):
            sobel_m = False

    if not log:
        cv2.imshow('connect LOG', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (k, k), sigmaX=x)
        Log = cv2.Laplacian(gray_blur, -1, ksize=5)
        frame_show = Log
        cv2.imshow('LOG', frame_show)
        if key == ord('e'):
            log = False

    if not gus:
        cv2.imshow('Connect Gaussian', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (k, k), sigmaX=x)
        frame_show = gray_blur
        cv2.imshow('Gaussian', frame_show)
        if key == ord('e'):
            gus = False

    if not sobel_thresh:
        cv2.imshow('Connect Sobel Threshold', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (k, k), sigmaX=x)
        sobelX = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=3)
        sobelY = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(sobelX, sobelY)
        magnitude = cv2.convertScaleAbs(magnitude)
        _, thresh = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)
        frame_show = thresh
        cv2.imshow('S', frame_show)
        if key == ord('e'):
            sobel_thresh = False

cap.release()
cv2.destroyAllWindows()
