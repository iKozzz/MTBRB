#!/bin/bash
echo "=== INSTALLING LIBS ==="
bash -c "sudo pip install django pillow"
bash -c "sudo apt update"
bash -c "sudo apt install -y python3-gpiozero"
echo "=== DONE INSTALLING LIBS ==="
echo "=== PREPARING STARTUP SCRIPTS ==="
bash -c "sudo chmod 755 start.sh stop.sh"
bash -c "sudo ln -s start.sh /etc/init.d/start_server"
bash -c "sudo update-rc.d start_server defaults"
echo "=== DONE PREPARING STARTUP SCRIPTS ==="
echo "=== CLEANING DIRECTORY ==="
bash -c "sudo rm -rf media/ db.sqlite3 em/migrations/0*"
echo "=== DONE CLEANING DIRECTORY ==="
echo "=== PREPARING DATABASE  ==="
bash -c "python manage.py makemigrations em"
bash -c "python manage.py sqlmigrate em 0001"
bash -c "python manage.py migrate em"
bash -c "python manage.py migrate"
echo "=== ALL DONE ==="