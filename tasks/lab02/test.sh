#!/bin/bash
source ~/nplenv/bin/activate
cd ~/npl/tasks/lab02/
head -n 1000 ~/npl/bigdata/part-00000 | ./mapper.py # > result
echo "Done!"
