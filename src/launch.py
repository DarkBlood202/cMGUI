import os,sys
from tkinter import *
from PIL import ImageTk,Image

DIR = sys.path[0]

# VENTANA RAIZ
root = Tk()
root.title("Chronicler's Maiden [Test Edition]")
root.iconphoto(True,PhotoImage(file=os.path.join(DIR,"..","data","128x.png")))
root.resizable(False,False)

WIDTH = 450
HEIGHT = 355

# CENTRAR VENTANA
screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

xCoord = int((screenW/2)-(WIDTH/2))
yCoord = int((screenH/2)-(HEIGHT/2))

root.geometry("{}x{}+{}+{}".format(WIDTH,HEIGHT,xCoord,yCoord))
#root.geometry("450x335")

# FRAME INTERIOR PRINCIPAL
framePrincipal = LabelFrame(root,text="Elija configuración",padx=10,pady=10)
framePrincipal.pack(pady=5,ipadx=50,padx=10)

# FRAME DE VIDAS Y BOMBAS
frameStocks = LabelFrame(framePrincipal,text="Personalizar parámetros",padx=61)
frameStocks.pack(pady=(1,10))

labelVidas = Label(frameStocks,text="Vidas:").grid(row=0,column=0)
labelBombas = Label(frameStocks,text="Ultimátums:").grid(row=1,column=0)

entradaVidas = Entry(frameStocks,width=5,borderwidth=1).grid(row=0,column=1,padx=5,pady=5) 
entradaBombas = Entry(frameStocks,width=5,borderwidth=1).grid(row=1,column=1,padx=5,pady=5)

boolVidasInf = BooleanVar()

chBVidasInf = Checkbutton(frameStocks,text="¿Infinitas?",variable=boolVidasInf)
chBVidasInf.deselect()
chBVidasInf.grid(row=0,column=2,padx=10,pady=5)

boolBombasInf = BooleanVar()

chBBombasInf = Checkbutton(frameStocks,text="¿Infinitos?",variable=boolBombasInf)
chBBombasInf.deselect()
chBBombasInf.grid(row=1,column=2,padx=10,pady=5)

# FRAME DE RECORRIDO
frameRecorrido = LabelFrame(framePrincipal,text="Tipo de recorrido",padx=1,pady=5)
frameRecorrido.pack()

recorridoCompleto = BooleanVar()
recorridoCompleto.set(True)

Radiobutton(frameRecorrido,text="Recorrido completo",variable=recorridoCompleto,value=True).grid(row=0,column=0)
Radiobutton(frameRecorrido,text="Recorrido Selectivo",variable=recorridoCompleto,value=False).grid(row=1,column=0)

labelNivel = Label(frameRecorrido,text="Nivel:").grid(row=1,column=1,columnspan=2,padx=(15,1))

niveles = ["1","2","3","4","5","6"]

nivel = IntVar()
nivel.set(niveles[0])

dropNiveles = OptionMenu(frameRecorrido,nivel,*niveles)
dropNiveles.grid(row=1,column=3)

boolSoloJefes = BooleanVar()

chBSoloJefes = Checkbutton(frameRecorrido,text="¿Solo jefes?",variable=boolSoloJefes)
chBSoloJefes.deselect()
chBSoloJefes.grid(row=1,column=4)

# FRAME DE MISCELANEA [EXTRAS]
frameExtra = LabelFrame(framePrincipal,text="Extras",padx=5)
frameExtra.pack(pady=(3,1))

desbloquearExtra = BooleanVar()

chBDesbloquearExtra = Checkbutton(frameExtra,text="Desbloquear modo Extra",variable=desbloquearExtra)
chBDesbloquearExtra.deselect()
chBDesbloquearExtra.grid(row=0,column=0)

boolPantallaCompleta = BooleanVar()

chBPantallaCompleta = Checkbutton(root,text="¿Pantalla Completa?",variable=boolPantallaCompleta)
chBPantallaCompleta.deselect()
chBPantallaCompleta.pack(pady=5)

botonIniciar = Button(root,text="¡Iniciar!").pack(pady=(1,5))

root.mainloop()