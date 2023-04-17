from tkinter import *

root=Tk()
root.title("calculator")

display=Entry(root)
display.grid(row=0,columnspan=5,sticky=W+E)
i=0
def imprimir_numero(numero):
    global i 
    display.insert(i,numero)
    i += 1

def limpiar_pantalla():
    display.delete(0,END)

def imprimir_operadores(operador):
    global i
    longitud_operador=len(operador)
    
    display.insert(i,operador)
    i += longitud_operador
# Botones númericos
Button(root,text="1",command=lambda:imprimir_numero(1)).grid(row=1,column=0,sticky=W+E)
Button(root,text="2",command=lambda:imprimir_numero(2)).grid(row=1,column=1,sticky=W+E)
Button(root,text="3",command=lambda:imprimir_numero(3)).grid(row=1,column=2,sticky=W+E)

Button(root,text="4",command=lambda:imprimir_numero(4)).grid(row=2,column=0,sticky=W+E)
Button(root,text="5",command=lambda:imprimir_numero(5)).grid(row=2,column=1,sticky=W+E)
Button(root,text="6",command=lambda:imprimir_numero(6)).grid(row=2,column=2,sticky=W+E)

Button(root,text="7",command=lambda:imprimir_numero(7)).grid(row=3,column=0,sticky=W+E)
Button(root,text="8",command=lambda:imprimir_numero(8)).grid(row=3,column=1,sticky=W+E)
Button(root,text="9",command=lambda:imprimir_numero(9)).grid(row=3,column=2,sticky=W+E)

# Otros botones


Button(root,text="AC",command=lambda:limpiar_pantalla()).grid(row=4,column=0,sticky=W+E)

Button(root,text="0",command=lambda:imprimir_numero(0)).grid(row=4,column=1,sticky=W+E)

Button(root,text="=",command=lambda:imprimir_numero(9)).grid(row=4,column=2,sticky=W+E)

Button(root,text="+",command=lambda:imprimir_operadores("+")).grid(row=1,column=3,sticky=W+E)

Button(root,text="*",command=lambda:imprimir_operadores("*")).grid(row=2,column=3,sticky=W+E)

Button(root,text="/",command=lambda:imprimir_operadores("/")).grid(row=3,column=3,sticky=W+E)

Button(root,text="-",command=lambda:imprimir_operadores("-")).grid(row=4,column=3,sticky=W+E)

root.mainloop()
