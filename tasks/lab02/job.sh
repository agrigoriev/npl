#!/bin/bash
hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=0 \
-input "/labs/facetz_2015_02_16" \
-file /home/alexey.grigoriev/npl/tasks/lab02/mapper.py -mapper mapper.py \
-output /users/adverts
