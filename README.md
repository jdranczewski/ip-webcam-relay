# ip-webcam-relay
Pipe the video from your phone to your Linux computer using the Android app
[IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en)
and one of the methods below.

## [`window.sh`](window.sh)
A simple, but more robust in testing solution, in which GStreamer is used to
pipe the video feed into a window; This can then be captured by [OBS](https://obsproject.com/)
for example.

This is a hack based on https://github.com/bluezio/ipwebcam-gst. Please use
it if it works for you, **it is a better solution**. I just couldn't get it
to work, so I took one part out of it.

## [`main.py`](main.py)
This uses opencv and pyfakewebcam instead, which produces an actual webcam and
can thus directly be used in video chatting applications. It's fast, but
occasional buffering issues were observed, causing the feed to go out of sync.

**Before using the script you have to execute [`config.sh`](config.sh)**.
