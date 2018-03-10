# PythonSerialSelector
Graphical serial port selector for python 3

1. This script will easily let you select serial port and save it into conf file.<br />
1. usage:<br />
	1. import serialSelect<br />
	2.  port = serialSelect.Select("conf.conf", 9600)<br />

This would open serial port "port" with baudrate 9600 and saved that port number into conf.conf so it can be preset on next startup.<br />
this script require "serial" and "tkinter" modules<br />
1. another arguments are these:<br />
	1. Select(path, baudrate, bytesize, stopbits, parity, timeout)<br />
	presets are:<br />
        - path = required<br />
        - baudrate = required<br />
        - bytesize = serial.EIGHTBITS<br />
        - stopbits = serial.STOPBITS_ONE<br />
        - parity = serial.PARITY_NONE<br />
        - timeout = None<br />
