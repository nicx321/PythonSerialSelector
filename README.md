# PythonSerialSelector
1. Graphical serial port selector for python 3<br \>

2. This script will easily let you select serial port and save it into conf file.<br \>
3. usage:<br \>
	import serialSelect<br \>
	port = serialSelect.Select("conf.conf", 9600)<br \>

4.This would open serial port "port" with baudrate 9600 and saved that port number into conf.conf so it can be preset on next startup.<br \>
	this script require "serial" and "tkinter" modules<br \>
5. another arguments are these:<br \>
	1. Select(path, baudrate, bytesize, stopbits, parity, timeout)<br \>
	presets are:<br \>
        	- path = required<br \>
        	- baudrate = required<br \>
       		- bytesize = serial.EIGHTBITS<br \>
        	- stopbits = serial.STOPBITS_ONE<br \>
        	- parity = serial.PARITY_NONE<br \>
        	- timeout = None<br \>
