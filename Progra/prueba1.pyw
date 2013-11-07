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
                        lista1.agregaPrimero(ver[1],d)import re





def busqueda(stg)
string1 = stg



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
