#!/bin/bash

# Arrange windows on the desktop for working

source ~/automation/helpers/arrange_windows_functions.sh

MUSIC_URL="https://www.youtube.com/watch?v=nMfPqeZjc2c&t=10622s&ab_channel=RelaxingWhiteNoise"
OPENAI_URL="https://chat.openai.com/?model=gpt-4"
# create array of urls
URLS=($MUSIC_URL $OPENAI_URL)

MESSAGER_APP_PATH="/snap/bin/slack"
NOTES_APP_PATH="/snap/bin/simplenote"

pkill brave
sleep 2

# Start browser
open_helper_browser
sleep 2
move_right_monitor
sleep 1
maximize_window

# Start apps
$MESSAGER_APP_PATH $NO_OUTPUT
sleep 3
move_left_monitor
sleep 1
move_sideways_right
sleep 1

$NOTES_APP_PATH $NO_OUTPUT
sleep 3
move_left_monitor
sleep 1
move_sideways_left
