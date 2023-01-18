import cv2
import os


captures=cv2.VideoCapture("video.mp4")
num_frames=0

if not os.path.exists("frames"):
    os.makedirs("frames")

while 1:
    ret,frame=captures.read()
    if ret==False:
        break
    num_frames+=1
    cv2.imwrite("frames/frame%d.jpg"%num_frames,frame)

captures.release()


imgs=[]
for i in range(1,num_frames+1):
    img=cv2.imread("frames/frame%d.jpg"%i)
    imgs.append(img)

height,width,layers=imgs[0].shape
video=cv2.VideoWriter('newvideo.mp4',cv2.VideoWriter_fourcc(*'mp4v'),50,(width,height))
for img in imgs:
    video.write(img)

video.release()