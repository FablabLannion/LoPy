#!/bin/bash
TTY=$1

ampy --port $TTY put config.py /flash/config.py
ampy --port $TTY put otaa_node.py /flash/main.py

miniterm.py $TTY 115200
