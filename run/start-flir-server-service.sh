#!/bin/bash
cd  /home/rov/git/FLIR-pubsub
nohup /home/rov/.virtualenvs/flir/bin/python -u run/flir-server.py  > /home/rov/logs/flir/flir.log 2>&1 < /dev/null