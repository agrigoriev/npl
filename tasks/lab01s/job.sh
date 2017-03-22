#!/bin/bash
source activate python2
cd ~/npl/tasks/lab01s/
ls
tail -n 10000 ~/npl/bigdata/advert.log | ./mapper.py | sort | ./reducer.py > result
echo "Done!"
