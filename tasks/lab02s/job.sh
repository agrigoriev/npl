#!/bin/bash
hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-streaming.jar \
-input "/labs/facetz_2015_02_12" \
-file ~/npl/tasks/lab02s/mapper.py -mapper mapper.py \
-file ~/npl/tasks/lab02s/reducer.py -mapper reducer.py \
-output "/user/alexey.grigoriev/top350"
