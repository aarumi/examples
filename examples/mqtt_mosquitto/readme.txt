
MOSQUITTO
=========

isntall server

sudo apt-get install mosquitto

install clients

sudo apt-get install mosquitto-clients

publisher & subscriptor

mosquitto_pub -h 192.168.100.1 -p 1883 -t "sensors/id" -m hola124

mosquitto_sub -h 192.168.100.1 -p 1883 -t "sensors/#"

MOSQUITTO PYTHON
================

sudo pip install paho-mqtt

