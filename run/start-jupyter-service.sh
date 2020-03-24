#!/bin/bash
nohup /home/rov/.virtualenvs/flir/bin/jupyter-notebook --config=/home/rov/.jupyter/jupyter_notebook_config.py > /home/rov/logs/jupyter/jupyter.log 2>&1 < /dev/null
