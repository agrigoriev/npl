#!/bin/bash
source ~/nplenv/bin/activate
cd ~/npl/tasks/lab02s/
head -n 1000 ~/npl/bigdata/part-00000 | ./mapper.py | sort | ./reducer.py > result
echo "Done!"
