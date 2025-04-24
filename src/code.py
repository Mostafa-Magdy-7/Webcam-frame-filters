import cv2
import numpy as np

cap = cv2.VideoCapture(0)
show_webcam = False
sobel_x=False
sobel_y=False
sobel_m=False
log=False
gus=False
sobel_thresh=False
x=10

# Create a black frame (480x640)
black_frame = np.zeros((480, 640, 3), dtype=np.uint8)

while True:

    key = cv2.waitKey(1) & 0xFF

    if key == ord('o'):
        show_webcam = True  
    if key == ord('x'):
        sobel_x=True
    if key == ord('y'):
        sobel_y=True
    if key == ord('m'):
        sobel_m=True
    if key == ord('l'):
        log=True 
    if key == ord('g'):
        gus=True  
    if key == ord('s'):
        sobel_thresh=True        
    if key == ord('+') or key == ord('='):  
        x += 1
    elif key == ord('-'):
        x= x-1   
                   
    if key == ord('q'):
        break
    if not show_webcam:
        
        cv2.imshow('Press O to Start Webcam', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
            break
        

        cv2.imshow('Webcam', frame)
        if key == ord('e'):
         show_webcam = False
         frame=black_frame

    if not sobel_x:
        
        cv2.imshow('x',black_frame)

    else:
        ret, frame = cap.read()
        if not ret:
            break



        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur=  cv2.GaussianBlur(gray , (3,3) ,sigmaX=x)
        sobelX=cv2.Sobel(gray_blur , cv2.CV_64F , 1,0 , ksize= 3)

        cv2.imshow('Sobel X', sobelX)
        if key == ord('e'):
         sobel_x = False
    
    
    if not sobel_y:
        
        cv2.imshow('connect to Y',black_frame)

    else:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur=  cv2.GaussianBlur(gray , ksize= (3,3) ,sigmaX= x)
        sobelY=cv2.Sobel(gray_blur , cv2.CV_64F , 0,1 , ksize= 3)

        cv2.imshow('Sobel Y', sobelY)
        if key == ord('e'):
         sobel_y = False



    if not sobel_m:
        
        cv2.imshow('Connectto magnitude',black_frame)

    else:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur =  cv2.GaussianBlur(gray , ksize= (3,3) ,sigmaX= x)
        sobelX=cv2.Sobel(gray_blur , cv2.CV_64F , 1,0 , ksize= 3)
        sobelY=cv2.Sobel(gray_blur , cv2.CV_64F , 0,1 , ksize= 3)
        mag = cv2.magnitude(sobelX , sobelY).astype(np.uint8)

        cv2.imshow('Magnitude', mag)
        if key == ord('e'):
         sobel_m = False

    if not log:
        
        cv2.imshow('connect LOG',black_frame)

    else:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur=  cv2.GaussianBlur(gray , ksize= (3,3) ,sigmaX= x)
        Log=cv2.Laplacian(gray_blur , -1 , ksize= 3)
        

        cv2.imshow('LOG', Log)
        if key == ord('e'):
         log = False

         

    if not gus:
        
        cv2.imshow('Connect Guassian ',black_frame)

    else:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur=  cv2.GaussianBlur(gray , ksize= (7,7) ,sigmaX= x)
       
        

        cv2.imshow('Guassian', gray_blur)
        
        if key == ord('e'):
         gus = False

         


    if not sobel_thresh:
      cv2.imshow('Connect sobel thresh', black_frame)
    else:
        ret, frame = cap.read()
        if not ret:
           break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (3, 3), sigmaX=float(x))
 
        sobelX = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=3)
        sobelY = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(sobelX, sobelY)

      # Normalize to 8-bit and apply threshold
        magnitude = cv2.convertScaleAbs(magnitude)
        _, thresh = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow('S', thresh)
        
        if key == ord('e'):
         sobel_thresh = False
    



   
    

cap.release()
cv2.destroyAllWindows()


