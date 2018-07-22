## MTBRB
сделано с любовью вместе с [Django](https://www.djangoproject.com)
---


[Подключение проводков](https://gpiozero.readthedocs.io/en/stable/recipes.html)
---
Библтотека `gpiozero` использует не физическую нумерацию пинов, а GPIO```[номер]```

![alt text](Raspberry-pi-pinout.jpg "Logo Title Text 1")


В нашем случае используется всего ``3`` провода.
Будем ориентироваться по **физическим** пинам.
* Ground - любая земля ```6, 9, 14, 20, 25```
* GPIO17 - кнопка старт ```11```
* GPIO18 - кнопка финиш ```12```

Запуск
---
Для первого запуска запустить: `./clean_and_init.sh`

это подготовит базу данных и приложение
 
затем создадим админа `python manage.py createsuperuser`

теперь появился доступ к `http://мой_ip(:мой_port)/admin` 

#### Использовать `./start.sh` или `./stop.sh` для управления сервером