import cv2, numpy
photo1 = cv2.imread('gateway.jpg')
photo2 = cv2.imread('goa.jpg')

#View Images
cv2.imshow('Pic1', photo1)
cv2.imshow('Pic2', photo2)
cv2.waitKey()
cv2.destroyAllWindows()

newimg = numpy.hstack((photo1, photo2))
cv2.imshow('NewImg', newimg)
cv2.waitKey()
cv2.destroyAllWindows()