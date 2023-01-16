import cv2
import os

# check if a folder named images exists
if not os.path.exists("images"):
    os.makedirs("images")

# capture the video from the webcam
cap = cv2.VideoCapture(0)

num_frames=0

while 1:
    ret,frame = cap.read()
    if ret==False:
        break
    # show the video
    cv2.imshow("video",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        print("Exiting...")
        break
    # if space bar is pressed, save the frame
    if k==ord(' '):
        cv2.imwrite("images/frame%d.jpg"%num_frames,frame)
        num_frames+=1

cap.release()
cv2.destroyAllWindows()

