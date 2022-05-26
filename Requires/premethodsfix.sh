#!/bin/bash

if ["$1"]; then 
    INTERFACE=$1
else
    INTERFACE="wlan0"    

ifconfig $INTERFACE down
airmon-ng check kill
ifconfig $INTERFACE down
iwconfig $INTERFACE mode managed
ifconfig $INTERFACE up
service NetworkManager start

