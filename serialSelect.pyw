import serial.tools.list_ports
import serial
from tkinter import *

port = None

def opport(path, baudrate, bytesize, stopbits, parity, PortS, SaveConf, timeout, xonxoff, rtscts, dsrdtr, tkvar):
    global port
    if SaveConf:
        with open(path,"w") as f:
            f.write(tkvar.get())
            f.write('\n')
    port = serial.Serial()
    port.port=tkvar.get()
    port.baudrate=baudrate
    port.bytesize=bytesize
    port.stopbits=stopbits
    port.parity=parity
    port.timeout=timeout
    port.xonxoff=xonxoff
    port.rtscts=rtscts
    port.dsrdtr=dsrdtr
    PortS.destroy()
        
def Select(baudrate, SaveConf=False, path=None, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
    PortS = Tk()
    PortS.geometry('240x60')
    PortS.title("Configurator")
    tkvar = StringVar(PortS)
    listp = serial.tools.list_ports.comports()
    connected = []
    choices = {}
    
    i=0
    for element in listp:
        choices[element.device]=i
        i+=1

    if i == 0:
        choices['None']=i
    if SaveConf:
        try:
            with open(path,"r+") as f:
                lines = f.readlines()
            lines[0] = lines[0].replace("\n", "")
        except:
            lines = [""]
    else:
        lines = [""]
        
    Label(PortS, text="COM port: ",font=(None,12)).place(x=35, y=4)
    inputt = OptionMenu(PortS, tkvar, *choices)
    inputt.place(x=130, y=0)
    if SaveConf and lines[0]!="":
        tkvar.set(lines[0])
    else:
        tkvar.set("Select")
        
    PortS.bind("<Return>", lambda event: opport(path, baudrate, bytesize, stopbits, parity, PortS, SaveConf, timeout, xonxoff, rtscts, dsrdtr, tkvar))
    B = Button(PortS, text="SET", command= lambda: opport(path, baudrate, bytesize, stopbits, parity, PortS, SaveConf, timeout, xonxoff, rtscts, dsrdtr, tkvar), width = 10)
    B.place(x=85, y=30)
    PortS.mainloop()
    return port
