#!/bin/bash

ifconfig wlan0 down
airmon-ng check kill
ifconfig wlan0 down
iwconfig wlan0 mode managed
ifconfig wlan0 up
service NetworkManager start

