def mostrar(gato):    
    for i in range(len(gato)):
        print gato[i]

def lanzamiento_X(gato, j):
    fila=int(raw_input("ingrese fila: "))
    columna=int(raw_input("ingrese columna: "))
    while fila > 2:
        fila=int(raw_input("ingrese fila: "))
    while columna > 2:
        columna=int(raw_input("ingrese columna: "))
    while gato[fila][columna] != "-":
        fila=int(raw_input("ingrese fila: "))
        columna=int(raw_input("ingrese columna: "))        
        while fila > 2:
            fila=int(raw_input("ingrese fila: "))
        while columna > 2:
            columna=int(raw_input("ingrese columna: "))
    if fila <= 2 and fila >= 0 and columna <= 2 and columna >= 0:
        gato[fila][columna] = "X"
        mostrar(gato)
        gg=GG_X(gato, j)
        return gg

def lanzamiento_O(gato, j):
    fila=int(raw_input("ingrese fila: "))
    columna=int(raw_input("ingrese columna: "))
    while fila > 2:
        fila=int(raw_input("ingrese fila: "))
    while columna > 2:
        columna=int(raw_input("ingrese columna: "))
    while gato[fila][columna] != "-":
        fila=int(raw_input("ingrese fila: "))
        columna=int(raw_input("ingrese columna: "))
        while fila > 2:
            fila=int(raw_input("ingrese fila: "))
        while columna > 2:
            columna=int(raw_input("ingrese columna: "))
    if fila <= 2 and fila >= 0 and columna <= 2 and columna >= 0:
        gato[fila][columna] = "O"
        mostrar(gato)
        gg=GG_O(gato, j)
        return gg

def GG_X(gato, j):
    if gato[0][0] == gato[0][1] and gato[0][0] == gato[0][2] and gato[0][0]=="X":
        print "Gana X"
        j = 10
    elif gato[1][0] == gato[1][1] and gato[1][0] == gato[1][2] and gato[1][0]=="X":
        print "Gana X"
        j = 10
    elif gato[2][0] == gato[2][1] and gato[2][0] == gato[2][2] and gato[2][0]=="X":
        print "Gana X"
        j = 10
    elif gato[0][0] == gato[1][1] and gato[0][0] == gato[2][2] and gato[0][0]=="X":
        print "Gana X"
        j = 10
    elif gato[0][2] == gato[1][1] and gato[0][2] == gato[2][0] and gato[0][2]=="X":
        print "Gana X"
        j = 10
    elif gato[0][0] == gato[1][0] and gato[0][0] == gato[2][0] and gato[0][0]=="X":
        print "Gana X"
        j = 10
    elif gato[0][1] == gato[1][1] and gato[0][1] == gato[2][1] and gato[0][1]=="X":
        print "Gana X"
        j = 10
    elif gato[0][2] == gato[1][2] and gato[0][2] == gato[2][2] and gato[0][2]=="X":
        print "Gana X"
        j = 10
    return j

def GG_O(gato, j):   
    if gato[0][0] == gato[0][1] and gato[0][0] == gato[0][2] and gato[0][0]=="O":
        print "Gana O"
        j = 10
    elif gato[1][0] == gato[1][1] and gato[1][0] == gato[1][2] and gato[1][0]=="O":
        print "Gana O"
        j = 10
    elif gato[2][0] == gato[2][1] and gato[2][0] == gato[2][2] and gato[2][0]=="O":
        print "Gana O"
        j = 10
    elif gato[0][0] == gato[1][1] and gato[0][0] == gato[2][2] and gato[0][0]=="O":
        print "Gana O"
        j = 10
    elif gato[0][2] == gato[1][1] and gato[0][2] == gato[2][0] and gato[0][2]=="O":
        print "Gana O"
        j = 10
    elif gato[0][0] == gato[1][0] and gato[0][0] == gato[2][0] and gato[0][0]=="O":
        print "Gana O"
        j = 10
    elif gato[0][1] == gato[1][1] and gato[0][1] == gato[2][1] and gato[0][1]=="O":
        print "Gana O"
        j = 10
    elif gato[0][2] == gato[1][2] and gato[0][2] == gato[2][2] and gato[0][2]=="O":
        print "Gana O"
        j = 10
    return j
        
#programa principal
gato = []
for i in range(3):
    linea = ["-"]*3
    gato.append(linea)
mostrar(gato)
j = 1
while j <= 9:
    if j%2 == 0:
        n=lanzamiento_O(gato, j)
        if n == 10:
            j = n
    else:
        n=lanzamiento_X(gato, j)
        if n == 10:
            j = n
    j += 1
