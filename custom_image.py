import cv2
import numpy as np
img = np.zeros((500,500, 3))
img[100:150, 100:150] = [0, 255, 0]
img[150:200, 150:200] = [255, 0, 0]
img[200:250, 200:250] = [0, 0, 255]
img[300:400, 300:400] = [255,255,255]
img[100:200, 300:400] = [0, 211, 11]
cv2.imshow('hii', img)
cv2.waitKey()
cv2.destroyAllWindows()