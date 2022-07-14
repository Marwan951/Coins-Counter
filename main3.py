import numpy as np
import cv2

img1 = cv2.imread("D:\F -  DISK\Downloads\coins.jpg", 0)
cv2.imshow("image", img1)
ret, thresh1 = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("thresholding", thresh1)
k = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(thresh1, k, iterations=7)
cv2.imshow("erosion", img_erosion)
(n, hierarchy) = cv2.findContours(img_erosion.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("#coins", len(n))
cv2.waitKey(0)
cv2.destroyAllWindows()
