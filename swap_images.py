import cv2, numpy
photo1 = cv2.imread('gateway.jpg')
photo2 = cv2.imread('goa.jpg')
print(photo1.shape)
print(photo2.shape)
cv2.imshow('Picture1', photo1)
cv2.imshow('Picture2', photo2)
cv2.waitKey()
cv2.destroyAllWindows()

#Swap Images Block
swap = photo1[30:100, 80:200]
photo2[30:100, 80:200] = swap
photo1[100:180, 200:320] = photo2[100:180, 200:320]

cv2.imshow('Picture1', photo1)
cv2.imshow('Picture2', photo2)
cv2.waitKey()
cv2.destroyAllWindows()