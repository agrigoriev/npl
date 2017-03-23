#!/bin/bash
cd ~/npl/tasks/lab01s/
tail -n 10000 ~/npl/bigdata/advert.log | ./mapper.py | sort | ./reducer.py > result
echo "Done!"
