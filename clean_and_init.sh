#!/bin/bash
echo "=== CLEANING DIRECTORY ==="
bash -c "sudo rm -rf media/ db.sqlite3 em/migrations/0*"
echo "=== DONE CLEANING DIRECTORY ==="
echo "=== PREPARING DATABASE  ==="
bash -c "python manage.py makemigrations em"
bash -c "python manage.py sqlmigrate em 0001"
bash -c "python manage.py migrate em"
echo "=== ALL DONE ==="