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
         print("Tabla dinamica")
         while nodo!=None:
           print( "Expresion")  
           print(nodo.expresion)
           print( "Valor")
           print(nodo.valor)
           print("\n")
           nodo=nodo.siguiente


               

def conformar(q,w):
    if q==None:
        return 0
    else:
        if re.search("[a-zA-Z]",q[0]):
            c=lista1.buscarenlista(q[0])
            if w[0]=="+":
                return c+conformar(q[1:],w[1:])
            if w[0]=="-":
                return c-conformar(q[1:],w[1:])
            if w[0]=="*":
                return c*conformar(q[1:],w[1:])
            if w[0]=="/":
                return c/conformar(q[1:],w[1:])
            if w==None:
                return c

            else:
                return 0
        else:
            c=int(q[0])
            if w[0]=="+":
                return c+conformar(q[1:],w[1:])
            if w[0]=="-":
                return c-conformar(q[1:],w[1:])
            if w[0]=="*":
                return c*conformar(q[1:],w[1:])
            if w[0]=="/":
                return c/conformar(q[1:],w[1:])
            if w==None:
                return 1
            else:
                return c




























def procesarinstructionbasic(str):
    
    ver=str.split()
    l=re.split("\w+",ver[3])
    if l[0]=="[":
         w=ver[3].split(";")
         lista1.agregaPrimero(ver[1],w[0])
    if l[0]!="[":
       if ver[2]=="=" and l[0]!="[" and ver[3]!="if"or ver[3]!="let" and len(ver)<4:
        a=procesarval(ver[3])
        almacenador=(ver[3]).split(";")
        if a>0:
            almacenador=(ver[3]).split(";")
            almacenador=int(almacenador[0])
            lista1.agregaPrimero(ver[1],almacenador)
        else:
             almacenador=(ver[3]).split(";")
             a=(almacenador[0]=="true")
             b=(almacenador[0]=="false")
             if (a==True)or(b==True):
                 lista1.agregaPrimero(ver[1],almacenador[0])
                 
            



            

def procesardinamic(str):
    
    ver=str.split()
    w=ver[3].split(";")
    a=re.split('\W+',w[0])
    b=re.split('\w+',w[0])
    l=re.split("\w+",ver[3])
    if l[0]!="[":
        if ver[2]=="=" and ver[3]!="if"or ver[3]!="let":
            if len(a)==1:
                if re.search("[a-zA-Z]",a[0]):
                    c=lista1.buscarenlista(a[0])
                    lista1.agregaPrimero(ver[1],c)
                if len(a)>1:
                    a=conformar(a,b[1:])
                    lista1.agregaPrimero(ver[1],a)


def procesartempif(str):
    ver=str.split()
    c=0
    a=False
    d=0
    w=0
    l=re.split("\w+",ver[3])
    if l[0]!="[":
      if ver[2]=="=" and ver[3]=="if":
        if re.search("[a-zA-Z]",ver[4]):
            c=lista1.buscarenlista(ver[4])
        else:
            c=int(ver[4])
            
        if ver[5]=="<":
            if re.search("[a-zA-Z]",ver[6]):
                d=lista1.buscarenlista(ver[6])
                a=c<d
                if a == True:
                    if re.search("[a-zA-Z]",ver[8]):
                        d=lista1.buscarenlista(ver[8])
                        lista1.agregaPrimero(ver[1],d)
                    else:
                        d=int(ver[8])
                        lista1.agregaPrimero(ver[1],d)
                        
                else:
                    if re.search("[a-zA-Z]",ver[10]):
                        d=lista1.buscarenlista(ver[10])
                        lista1.agregaPrimero(ver[1],d)
                    else:
                        d=int(ver[10])
                        lista1.agregaPrimero(ver[1],d)
            else:
                d=lista(ver[6])
                a=c<d
                if a == True:
                    if re.search("[a-zA-Z]",ver[10]):
                        d=lista1.buscarenlista(ver[10])
                        lista1.agregaPrimero(ver[1],d)
                    else:
                        d=int(ver[10])
                        lista1.agregaPrimero(ver[1],d)
                        
                else:
                    if re.search("[a-zA-Z]",ver[10]):
                        d=lista1.buscarenlista(ver[10])
                        lista1.agregaPrimero(ver[1],d)
                    else:
                        d=int(ver[10])
                        lista1.agregaPrimero(ver[1],d)

        if ver[5]==">":
             if re.search("[a-zA-Z]",ver[6]):
                d=lista1.buscarenlista(ver[6])
                a=c>d
                if a == True:
                    if re.search("[a-zA-Z]",ver[8]):
                        d=lista1.buscarenlista(ver[8])
                        
                        lista1.agregaPrimero(ver[1],d)
                       
                        
                    else:
                        d=int(ver[8])
                        lista1.agregaPrimero(ver[1],d)
                else:
                     ve=ver[6:]
                     while ve!="else":
                         ve=ver[1:]
                     if re.search("[a-zA-Z]",ve[1]):
                        d=lista1.buscarenlista(ve[1])
                        lista1.agregaPrimero(ver[1],d)
                     else:
                         d=int(ve[1])
                         lista1.agregaPrimero(ver[1],d)  
             else:
                  d=int(ver[6])
                  a=c<d
                  if a == True:
                    if re.search("[a-zA-Z]",ver[8]):
                        d=lista1.buscarenlista(ver[8])
                        lista1.agregaPrimero(ver[1],d)
                    else:
                        d=int(ver[8])
                        lista1.agregaPrimero(ver[1],d)
                  else:
                     ve=ver[6:]
                     while ve!="else":
                         ve=ver[1:]
                     if re.search("[a-zA-Z]",ve[1]):
                        d=lista1.buscarenlista(ve[1])
                        lista1.agregaPrimero(ver[1],d)
                     else:
                        d=int(ve[1])
                        lista1.agregaPrimero(ver[1],d)

















# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.

infile = open('hola.txt', 'r')
infile2 = open('hola.txt', 'r')
infile3 = open('hola.txt', 'r')
global lista1
lista1=ListaEnlazada()
# Mostramos por pantalla lo que leemos desde el fichero
for line in infile:
    procesarinstructionbasic(line)


for line in infile2:
    procesardinamic(line)

for line in infile3:
    procesartempif(line)      
    
    
# Cerramos el fichero.
infile.close()
infile2.close()
infile3.close()

lista1.imprimir()

def procesarlineaval(str):
    ver=str.split()
    determinar=0
    while (len (ver))>0:
          a=procesarval(ver[determinar])
          ver=ver[1:]





        

