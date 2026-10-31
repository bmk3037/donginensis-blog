#!/usr/bin/env bash
c=$1; mkdir -p clip/$c
ffmpeg -y -loglevel error -i clipsrc/$c.mp4 -vf "minterpolate=fps=60:mi_mode=mci,scale=720:1280" -q:v 4 -frames:v 476 clip/$c/%03d.jpg && echo $c done
