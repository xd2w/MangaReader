#!/bin/bash

InstDIR=
currDIR=$(pwd)

cd $InstDIR

source ../venv/bin/activate
nohup waitress-serve --host 0.0.0.0 --port 8000 --threads 6 reader:app &>> logs/waitress.log &

cd $currDIR
