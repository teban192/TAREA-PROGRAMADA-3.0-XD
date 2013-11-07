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
           if nodo.valor==str:
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

    def Funcion2(self):
        nodo=self.cabeza
        while (nodo != None):
            try:
                #procesarinstructionbasic2(nodo.valor)
                print '%s' % is_number(nodo.valor)
                print '%s' % Funcion(nodo.valor)
            except:
                print 'error de identificacion'
            nodo=nodo.siguiente
            
def procesarinstructionbasic(str):
    ver=str.split()
    try:
        if ver[2]=="=" and ver[3]!="if"or ver[3]!="let" and len(ver)<4:
            lista1.agregaPrimero(ver[1],ver[3])
    except:
        lista2.append
        
def procesarinstructionbasic2(str):
    ver=str.split()
    if ver[1]==";" and len(ver)<2:
        lista2.agregaPrimero(ver[1],ver[0])
        lista2.imprimir()

def Funcion(nodo):
        try:
            if (nodo.valor) == int(nodo.valor):
                return 'Es entero'
            else:
                return 'No es entero'
        except:
                print 'No ha sido evaluado'

def is_number(nodo):
    try:
        print(nodo)
        float(nodo)
        return 'Es Numero'
    except ValueError:
        return 'No Es Numero'
        #expresion(nodo.valor)

#def expresion(nodo):
    

        
# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.

infile = open('first.sml', 'r')
global lista1
global lista2
lista1=ListaEnlazada()
lista2=[]
# Mostramos por pantalla lo que leemos desde el fichero
for line in infile:
    procesarinstructionbasic(line)
    
# Cerramos el fichero.
infile.close()
lista1.imprimir()
lista1.Funcion2()

def procesarlineaval(str):
    ver=str.split()
    determinar=0
    while (len (ver))>0:
          a=procesarval(ver[determinar])
          ver=ver[1:]
          
def procesarval(s):
    try:
        i = int(s) 
    except ValueError:
        i = 0 
    return i
