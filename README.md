# PythonSerialSelector
Graphical serial port selector for python 3

This script will easily let you select serial port and save it into conf file.
usage
    import serialSelect
	port = serialSelect.Select("conf.conf", 9600)

This would open serial port "port" with baudrate 9600 and saved that port number into conf.conf so it can be preset on next startup.
this script require "serial" and "tkinter" modules
another arguments are these:
		Select(path, baudrate, bytesize, stopbits, parity, timeout)
		presets are:
				path = required
				baudrate = required
				bytesize = serial.EIGHTBITS
				stopbits = serial.STOPBITS_ONE
				parity = serial.PARITY_NONE
				timeout = None
  
