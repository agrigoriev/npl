#!/bin/bash
source ~/nplenv/bin/activate
cd ~/npl/tasks/lab02/
cat ~/npl/bigdata/part-00000 | ./mapper.py # > result
echo "Done!"
