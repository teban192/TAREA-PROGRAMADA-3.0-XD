import re


def procesarval(s):
    w=s.split(";")
    try:
        i = int(w[0]) 
    except ValueError:
        i = 0 
    return i


class Nodo:
    def __init__(self, expresion=None,valor=None, siguiente=None):
        self.expresion = expresion
        self.valor= valor
        self.siguiente = siguiente



class ListaEnlazada :
    def __init__(self) :
        self.longitud = 0
        self.cabeza = None
    def agregaPrimero(self, expresion,valor):
        nodo = Nodo(expresion,valor)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.longitud = self.longitud + 1
    def buscarenlista(self,str):
        nodo=self.cabeza
        while nodo!=None:
           if nodo.expresion==str:
               return nodo.valor
           else:
               nodo=nodo.siguiente

    def imprimir(self):
         nodo=self.cabeza
         while nodo!=None:
           print(nodo.expresion)
           print(nodo.valor)
           print("\n")
           nodo=nodo.siguiente


               



def procesarinstructionbasic(str):
    
    ver=str.split()
    if ver[2]=="=" and ver[3]!="if"or ver[3]!="let" and len(ver)<4:
        a=procesarval(ver[3])
        if a>0:
            almacenador=(ver[3]).split(";")
            almacenador=int(almacenador[0])
            lista1.agregaPrimero(ver[1],almacenador)

def procesardinamic(str):
    
    ver=str.split()
    a=ver[3].split(";")
    a=re.split('\W+',a[0])
    if ver[2]=="=" and ver[3]!="if"or ver[3]!="let":

        if len(a)==1:
           if re.search("[a-zA-Z]",a[0]):
               c=lista1.buscarenlista(a[0])
               lista1.agregaPrimero(ver[1],c)
       

            
        

# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.

infile = open('hola.txt', 'r')
infile2 = open('hola.txt', 'r')
global lista1
lista1=ListaEnlazada()
# Mostramos por pantalla lo que leemos desde el fichero
for line in infile:
    procesarinstructionbasic(line)


for line in infile2:
    procesardinamic(line)   
    
    
# Cerramos el fichero.
infile.close()
lista1.imprimir()

def procesarlineaval(str):
    ver=str.split()
    determinar=0
    while (len (ver))>0:
          a=procesarval(ver[determinar])
          ver=ver[1:]





        

