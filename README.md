# PythonSerialSelector
1. Graphical serial port selector for python 3

2. This script will easily let you select serial port and save it into conf file.
3. usage:
	```
	import serialSelect
	port = serialSelect.Select(9600)
	```
	Or
	```
	import serialSelect
	port = serialSelect.Select(9600, True, "conf.conf")
	```

4. This would open serial port "port" with baudrate 9600 and saved that port number into conf.conf so it can be preset on next startup.
	this script require "serial" and "tkinter" modules
5. another arguments are these:
	* Select(baudrate, SaveConf, path, bytesize, stopbits, parity, timeout)
	* presets are:
		- baudrate = required
		- SaveConf = False
		- path = None, required if SaveConf = True
		- bytesize = serial.EIGHTBITS
		- stopbits = serial.STOPBITS_ONE
		- parity = serial.PARITY_NONE
		- timeout = None
		