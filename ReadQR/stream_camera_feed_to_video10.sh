# this has to be a parralell process that is done and can be setup on different ways
# make sure "fuser /dev/video10" is empty before running this 
#!/bin/bash

### this part is to make sure it workes the second time ###
# Kill any process using /dev/video10
sudo fuser -k /dev/video10
# Remove the kernel module completely
sudo modprobe -r v4l2loopback
# (Optional safety) wait a sec
sleep 1

### main ###
# Load virtual camera kernel module
sudo modprobe v4l2loopback video_nr=10 card_label="VirtualCam" exclusive_caps=1
# Start libcamera-vid and pipe to FFmpeg, which streams to the virtual camera
libcamera-vid -t 0 --width 1280 --height 720 --inline --codec yuv420 --nopreview -o - | \
ffmpeg -f rawvideo -pix_fmt yuv420p -s 1280x720 -r 30 -i - \
-f v4l2 -vcodec rawvideo /dev/video10
