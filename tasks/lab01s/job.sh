#!/bin/bash
hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-streaming.jar \
  -D mapred.reduce.tasks=1 \
  -input /users/adverts \
  -output /users/adverts/result \
  -mapper "mapper.py" \
  -reducer "reducer.py"
