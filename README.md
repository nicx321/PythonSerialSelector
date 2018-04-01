# PythonSerialSelector
1. Graphical serial port selector for python 3

2. This script will easily let you select serial port and save it into conf file.
3. usage:
	```
	import serialSelect
	port = serialSelect.Select("conf.conf", 9600)
	```

4. This would open serial port "port" with baudrate 9600 and saved that port number into conf.conf so it can be preset on next startup.
	this script require "serial" and "tkinter" modules
5. another arguments are these:
	* Select(baudrate, bytesize, stopbits, parity, timeout, path, SaveConf)
	* presets are:
		- baudrate = required
		- SaveConf = False
		- bytesize = serial.EIGHTBITS
		- stopbits = serial.STOPBITS_ONE
		- parity = serial.PARITY_NONE
		- timeout = None
		- path = None, required if SaveConf = True
		