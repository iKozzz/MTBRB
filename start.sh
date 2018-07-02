#!/bin/bash
IP="$(hostname -I | cut -d' ' -f1):80"
bash -c "nohup sudo python manage.py runserver $IP &>/dev/null &"
echo "Application should start in a seconds!"