import os
import cv2
files = os.listdir(os.getcwd())
relevant_files = [x for x in files if x.endswith('.jpeg')]
for filename in relevant_files:
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:,:,2]

    T = cv2.ximgproc.niBlackThreshold(gray, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=81, k=0.1, binarizationMethod=cv2.ximgproc.BINARIZATION_WOLF)
    grayb = (gray > T).astype("uint8") * 255

    cv2.imwrite(f"improved_{filename}.jpeg", grayb)