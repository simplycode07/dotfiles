#!/bin/sh
# xrandr -s 1680x1050 &
picom -b &

touchpad_id=$( xinput list | grep "Touchpad" | grep -o -P "id=\d\d" | grep -o -P "\d\d" )

xinput set-prop	$touchpad_id 301 0.05
