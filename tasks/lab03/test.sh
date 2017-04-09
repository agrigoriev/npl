#!/bin/bash
source ~/projects/nplenv/bin/activate
cd ~/projects/npl/tasks/lab03/
cat ~/projects/npl/bigdata/part-00000 | ./mapper.py # > result
echo "Done!"
