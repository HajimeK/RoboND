import matplotlib.pyplot as plt
import cv2
import numpy as np
# img = cv2.imread('sample.jpg')
# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
# #OR
# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)


# img = cv2.imread('sample.jpg')
# rows,cols = img.shape[:2]
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## rotate
# img = cv2.imread('sample.jpg',0)
# rows,cols = img.shape[:2]
# M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# dst = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## Affine
# img = cv2.imread('sample.jpg')
# rows,cols,ch = img.shape
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread('sample.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
