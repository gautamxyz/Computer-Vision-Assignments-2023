# Assignment-1 Report

## Task-1

Here we use `cv.imread()` to load the images. Then in the first image(image of the beach) we select a rectangle by selecting number of consecutive rows like 50 to 100 and correspondingly selecting columns like 100 to 400. This makes the horizontal rectangle and similarly we draw a vertical rectangle by selecting rows from 100 to 350 and columns from 225 to 275. For both of these rectangles we make the pixels of the image to be 0 (black). This creates a T shaped hole in image 1 and then for the same 2 rectangles we make their pixels to be equal to the corresponding pixel values of image 2. Thus the T shaped hole in image 1 is filled with details from image 2.

`cv2.imshow('image1',img1)` displays the manipulated image 1 in a window and `cv2.waitKey(0)` waits for a key to be pressed to close the window.

## Task-2
`cv2.VideoCapture("video.mp4")` is used to capture the video from the "video.mp4" file. We initialize a variable named `num_frames` to keep track of the number of frames in the video. We create a directory named `frames` to store all the frames in the video. Then we use a while loop to iterate over all the frames in the video. We use `cv2.imwrite()` to save the frames in the `frames` directory. We do this as long as `captures.read()` continues to return `True`. The frames are numbered as frame1, frame2 etc. `captures.release()` is used to release the video capture object. 

For the second part, we initialize an empty array called `imgs`. We iterate over the frames saved in the frames folder and use `cv2.imread()` to read the frames and append them to the `imgs` array. We find the shape of the images using `imgs[0].shape` and initialize a variable `height` to store the height of the images, width to store the width of the image and the number of layers(channels) in the image. We then use the `cv2.VideoWriter()` function to initialize the video object. It takes the arguments as 

1. The name of the output video file
2. Video codec specified by fourcc
3. fps
4. Dimensions of the video

We use `video.write()` to write the frames saved in `imgs` array to the video. We use `video.release()` to release the video object. The new video gets saved in the same directory.

It is observed that with high fps, the video moves faster and with low fps it moves slower. Thus the duration of the video is inversely proportional to the fps.

## Task-3
We use `cv2.VideoCapture(0)` to capture video from webcam and create an object named `cap` and initialize `num_frames` to 0. We run a while loop as long as the frames are being capture i.e. the value returned by `cap.read()` is true. `cv2.imshow` is used to display the video side by side as it is being captured by our webcam. We the use `cv2.waitkey(1)` to wait for a key to be pressed. If the key pressed is `q` then we break out of the loop and release the video capture object. If the key pressed is spacebar then we save the frame in the `images` directory and increment the `num_frames` variable. We use `cv2.imwrite()` to save the frame in the `frames` directory. We use `cv2.destroyAllWindows()` to close all the windows.

Link to media files : `https://drive.google.com/file/d/1lBhlvKG-BCOqkAHdYbBdhMQPHRaQxeAM/view?usp=sharing`