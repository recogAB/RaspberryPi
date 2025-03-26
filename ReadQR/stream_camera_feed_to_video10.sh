# this has to be a parralell process that is done and can be setup on different ways
sudo modprobe v4l2loopback video_nr=10 card_label="VirtualCam" exclusive_caps=1
libcamera-vid -t 0 --width 1280 --height 720 --inline -o - | \
ffmpeg -i - -f v4l2 /dev/video10