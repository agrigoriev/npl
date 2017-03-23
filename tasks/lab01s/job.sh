#!/bin/bash
hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-input /users/advert \
-file /home/hdfs/npl/tasks/lab01s/mapper.py -mapper mapper.py \
-file /home/hdfs/npl/tasks/lab01s/reducer.py -reducer reducer.py \
-output /users/adverts
