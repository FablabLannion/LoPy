#!/bin/bash
TTY=$1

ampy --port $TTY put config.py /flash/config.py
ampy --port $TTY put main.py /flash/main.py
ampy --port $TTY put nanogateway.py /flash/nanogateway.py

miniterm.py $TTY 115200
