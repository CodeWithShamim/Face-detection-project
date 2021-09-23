import cv2 as cv

'''
img = cv.imread("image/azazul.jpg")
cv.imshow("Brothers-pic!!", img)
cv.waitKey(0)
'''


#-----------------------------------
 
img = cv.imread("image/azazul.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img, (19,19), 0)

cv.imshow("Brothers-pic!!", img)
cv.imshow("Brothers-gray-pic!!", img_gray)
cv.imshow("Brothers-blur-pic!!", img_blur)

cv.waitKey(0)