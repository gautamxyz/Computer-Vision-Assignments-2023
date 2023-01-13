import cv2

img1=cv2.imread("beach.jpeg")
img2=cv2.imread("mountain.jpeg")

img1[50:100,100:400]=0
img1[100:350,225:275]=0

img1[50:100,100:400]=img2[50:100,100:400]
img1[100:350,225:275]=img2[100:350,225:275]
cv2.imshow("img1",img1)
cv2.waitKey(0)