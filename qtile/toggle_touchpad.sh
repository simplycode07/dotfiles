#!/bin/bash

touchpad_id=$( xinput list | grep "Touchpad" | grep -o -P "id=\d\d" | grep -o -P "\d\d" )
state=$( xinput list-props $touchpad_id | grep "Device Enabled" | grep -o "[01]$" )
echo $state

if [ "$state" -eq '1' ];then
    xinput --disable $touchpad_id && notify-send "TouchPad Disabled" -t 1500
else
    xinput --enable $touchpad_id && notify-send "TouchPad Enabled" -t 1500
fi
