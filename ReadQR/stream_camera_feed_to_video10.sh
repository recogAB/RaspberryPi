# this has to be a parralell process that is done and can be setup on different ways
#!/bin/bash

# Load virtual camera kernel module
sudo modprobe v4l2loopback video_nr=10 card_label="VirtualCam" exclusive_caps=1

# Start libcamera-vid and pipe to FFmpeg, which streams to the virtual camera
libcamera-vid -t 0 --width 1920 --height 1080 --codec yuv420 --inline --framerate 30 -o - | \
ffmpeg -f rawvideo -pix_fmt yuv420p -s 1920x1080 -r 30 -i - -f v4l2 /dev/video10