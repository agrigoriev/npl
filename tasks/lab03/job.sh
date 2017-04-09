#!/bin/bash
hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-streaming.jar \
 -D mapred.reduce.tasks=0 -input "/labs/lab03data" \
-file ~/npl/tasks/lab03/mapper.py -mapper mapper.py \
-output /user/alexey.grigoriev/lab03
