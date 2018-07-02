#!/bin/bash

mtb_pid=$(pgrep -f "sudo python manage.py" | sed "s/\(\d*\) .*/\1/")

if [ -z "$mtb_pid" ]
then
  msg="OK. No MTB Server process found"
else
  bash -c "sudo kill $mtb_pid"
  msg="1 - DONE. MTB Server should be dead now."
fi
echo ${msg}

mtb_pid=$(pgrep -f "python" | sed "s/\(\d*\) .*/\1/")

if [ -z "$mtb_pid" ]
then
  msg="OK. No MTB Server process found"
else
  bash -c "sudo kill $mtb_pid"
  msg="2 - DONE. MTB Server should be dead now."
fi
echo ${msg}