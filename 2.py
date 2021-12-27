import cv2
import argparse
import imutils
data = cv2.imread("/home/pi/image2.jpg")
resized = imutils.resize(data,width=600)
data_gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(data_gray,1,10)
thresh = cv2.threshold(data_gray,115,235,cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = resized.copy()
for c in cnts:
    cv2.drawContours(output,[c],-1,(0,0,255),3)
    cv2.imshow("cnts",output)
    cv2.waitKey(0)
text = "I found {} objects".format(len(cnts))
cv2.putText(output,text,(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),1)
cv2.imshow("edged",edged)
cv2.imshow("gray",data_gray)
cv2.imshow("data",resized)
cv2.imshow("threshold",thresh)
cv2.imshow("textput",output)
cv2.waitKey(0)
