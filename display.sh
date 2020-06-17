#!/bin/bash

sudo modprobe v4l2loopback devices=1
adb forward tcp:1224 tcp:8080
gst-launch-1.0 souphttpsrc location=http://127.0.0.1:1224/videofeed do-timestamp=true is-live=true ! queue ! multipartdemux ! decodebin ! videoconvert ! ximagesink
