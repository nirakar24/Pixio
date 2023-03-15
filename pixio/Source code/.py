import cv2 as cv

img=cv.imread("C:\Volume E\Projects\Code-A-Thon\LBL001_Code-A-Thon\Frontend\images\Idea-2")

status = cv.imwrite("C:/Sample/temp/new_image.jpg",img)
print(status)
