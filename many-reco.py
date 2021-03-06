import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('D:\python\images\guru.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('D:\python\images\logo.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('image', img_rgb) 
k = cv2.waitKey(0) & 0xFF

# wait for ESC key to exit 
if k == 27: 
	cv2.destroyAllWindows() 
	
# wait for 's' key to save and exit 
elif k == ord('s'): 
	cv2.imwrite('new.png',img_rgb) 
	cv2.destroyAllWindows() 
