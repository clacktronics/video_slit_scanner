import cv2
import numpy as np
from sys import argv

STRIP_W = 1



video = cv2.VideoCapture(argv[1])

success,img = video.read()
print success
im_h, im_w, im_c = img.shape

strip = im_w / 2

#print dir(cv2)

frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

output_img = np.zeros((im_h,frames,3), np.uint8)



success = True
for count in range(frames/4):

    try:
        success,img = video.read()
        output_img[0:im_h,count:count+STRIP_W] = img[0:im_h,strip:strip+STRIP_W]
        del strip
        strip = 0
        print "%d / %d " % (count,frames)
    except Exception as e:
        print e
        break
    except KeyboardInterrupt:
        break

cv2.imwrite("stripscan.jpg", output_img)
