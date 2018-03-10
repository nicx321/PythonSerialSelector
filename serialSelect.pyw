import serial.tools.list_ports
import serial
from tkinter import *

path = None
inputt = None
baudratei = None
bytesizei = None
stopbitsi = None
parityi = None
PortS = None
timeouti=None
port = None

def opport():
    global inputt, path, baudratei, baudratei, bytesizei, stopbitsi, parityi, PortS, port
    with open(path,"w") as f:
        f.write(inputt.get())
        f.write('\n')
    port = serial.Serial(port=inputt.get(),
                baudrate=baudratei,
                bytesize=bytesizei,
                stopbits=stopbitsi,
                parity=parityi,
                timeout=None)
    PortS.destroy()
        
def Select(pathi, baudrateii, bytesizeii=serial.EIGHTBITS, stopbitsii=serial.STOPBITS_ONE, parityii=serial.PARITY_NONE, timeoutii=None):
    global inputt, path, baudratei, bytesizei, stopbitsi, parityi, PortS, port
    
    inputt = inputt
    path = pathi
    baudratei = baudrateii
    bytesizei = bytesizeii
    stopbitsi = stopbitsii
    parityi = parityii
    timeouti=timeoutii

    PortS = Tk()
    PortS.title("Configurator")
    listp = serial.tools.list_ports.comports()
    connected = []
    for element in listp:
        connected.append(element.device)
    try:
        with open(path,"r+") as f:
            lines = f.readlines()
        lines[0] = lines[0].replace("\n", "")
    except:
        lines = [""]
        
    Label(PortS, text="COM ports: "+str(connected)).grid(row=0, column=0)
    inputt = Entry(PortS)
    inputt.grid(row=0, column=1)
    inputt.insert(END, lines[0])
    Button(PortS, text="SET", command=opport, width = 10).grid(row=2, column=0, sticky=N+S, columnspan=2)
    PortS.mainloop()

    return port

    
