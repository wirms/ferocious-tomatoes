# Makefile for the project

setup:
	sudo apt-get install python-smbus
	cd ./dependencies/Adafruit-Motor-HAT-Python-Library && sudo python ./setup.py install

hardware-test:
	python tests/motor-test.py