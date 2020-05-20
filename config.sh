#!/bin/bash

sudo modprobe v4l2loopback devices=2
adb forward tcp:1224 tcp:8080
