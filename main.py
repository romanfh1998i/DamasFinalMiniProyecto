class matrix:

     def printMatrix(self, Matrix):
         print("\n\n")
         print("------------------Damas_Cinncinatus-----------")
         print("\n")
         print("0 |  1  |  2  |  3  |  4  |  5  |  6  |  7 \n")
         print("--------------------------------------------")
         for fila in Matrix:
             print("  |  ".join(map(str,fila)))
             print("-------------------------------------------")
         print("\n")
         print("")
         print("\n\n")
#aqui se instancia el tablero osea que se hace un llamado de la funcion de arriba  que donde se imprime el tablero

Matrix =[[]]
Matrix =[[' ' for x in range(8)] for y in range(8)]
n1 = [0, 2, 4, 6]
n2 = [1, 3, 5, 7]
 # p es igual a posicion
for p in n1:
     Matrix[0][p] = "X"
     Matrix[2][p] = "X"
     Matrix[6][p] = "O"
for p in n2:
     Matrix[1][p] = "X"
     Matrix[5][p] = "O"
     Matrix[7][p] = "O"
p = matrix()
p.printMatrix(Matrix)
class movimiento:
    def __init__(self,movimientoDerecha,movimientoIzquierda,cutderecha,cutIzquierda):
        self.x=[]
        self.y=[]
        self.movimientoDerecha=movimientoDerecha
        self.movimientoIzquierda=movimientoIzquierda
        self.cutderecha=cutderecha
        self.cutIzquierda=cutIzquierda
        self.respuesta=[]

    def movimientox(self):
        self.movimientoDerecha=False
        self.movimientoIzquierda=False
        self.cutderecha=False
        self.cutIzquierda=False
        self.respuesta=""
        def movimientoX(self):
            print("X turno ")
            x = int(input("Entra el numero fila:"))
            y = int(input("Entra el numero columna:"))
            if(str(Matrix[x][y])=="x"):
                    if(not y ==7 and not y==0):
                        self.movimientoDerecha=True
                        if(str(Matrix[x+1][y+1])==" "):
                            self.movimientoIzquierda=True
                        if(str(Matrix[x+1][y-1])==" "):
                            self.movimientoIzquierda=True
                    elif(y==7):
                        if(str(Matrix[x+1][y-1])==" "):
                            self.movimientoDerecha=True
                    else:
                        if(str(Matrix[x+1][y+1])==" "):
                            self.movimientoDerecha=True
                    if(not y>5 and not y<2):
                        if(str(Matrix[x+1][y+1])=="O"and not str(Matrix[x+2][y+2])=="O"and not str(Matrix[x+2][y+2])=="X"):
                            self.cutderecha=True
                        if(str(Matrix[x+1][y-1])=="O"and not str(Matrix[x+2][y-2])and not str(Matrix[x+2][y-2])=="X"):
                            self.cutIzquierda=True
                    elif(y>5):
                        if(str(Matrix[x+1][y-1])=="O"and not str(Matrix[x+2][y-2])=="O"and not str(Matrix[x+2][y-2])=="X"):
                            self.cutIzquierda=True
                    else:
                        if(str(Matrix[x+1][y+1])=="O"and not str(Matrix[x+2][x-2])=="O"and not str(Matrix[x+2][y+2])=="X"):
                            self.cutderecha=True
                    if(any([self.cutderecha,self.cutIzquierda])):
                        self.movimientoDerecha=False
                        self.movimientoIzquierda=False
                    if(any([self.movimientoIzquierda,self.movimientoDerecha])):
                        if(self.movimientoIzquierda):
                            if(self.movimientoDerecha):
                                self.respuesta=input("Movimiento Derecha o Izquierda ?, Si es Derecha o Izquierda , si es Derecha responder con D y si es Izquierda con I ")
                                self.respuesta=self.respuesta.upper()
                            else:
                                self.respuesta="I"
                        else:
                            self.respuesta="D"
                    if(any([self.respuesta=="D",self.respuesta=="I"])):
                        if(self.respuesta=="D"):
                            Matrix[x+1][y+1]="X"
                            Matrix[x][y]=" "
                            p.printMatrix(Matrix)
                        else:
                            Matrix[x+1][y-1]="X"
                            Matrix[x][y]=" "
                            p.printMatrix(Matrix)
                    elif(any([self.cutderecha,self.cutIzquierda])):
                        if(self.cutIzquierda):
                            if(self.cutderecha):
                                self.respuesta=input("Movimiento Derecha o Izquierda ?, Si es Derecha o Izquierda , si es Derecha responder con D y si es Izquierda con I ")
                                self.respuesta=self.respuesta.upper()
                            else:
                                self.respuesta="D"
                        else:
                            self.respuesta="I"
                    if(any([self.respuesta=="D",self.respuesta=="I"])):
                        if(self.respuesta=="D"):
                            Matrix[x+1][y+1]=" "
                            Matrix[x+2][y+2]="X"
                            p.printMatrix(Matrix)
                        else:
                            Matrix[x+1][y-1]=" "
                            Matrix[x+2][y-2]="X"
                            p.printMatrix(Matrix)
                    if (not y > 5 and not y < 2):
                        if (str(Matrix[x + 1][y + 1]) == "O" and not str(Matrix[x + 2][y + 2]) == "O" and not str(
                                Matrix[x + 2][y + 2]) == "X"):
                            self.cutderecha = True
                        if (str(Matrix[x + 1][y - 1]) == "O" and not str(Matrix[x + 2][y - 2]) and not str(
                                Matrix[x + 2][y - 2]) == "X"):
                            self.cutIzquierda = True
                    elif (y > 5):
                        if (str(Matrix[x + 1][y - 1]) == "O" and not str(Matrix[x + 2][y - 2]) == "O" and not str(
                                Matrix[x + 2][y - 2]) == "X"):
                            self.cutIzquierda = True
                    else:
                        if (str(Matrix[x + 1][y + 1]) == "O" and not str(Matrix[x + 2][x - 2]) == "O" and not str(
                                Matrix[x + 2][y + 2]) == "X"):
                            self.cutderecha = True
            else:
                        print("movimiento incorrecto")
                        movimientoX(self)

        def movimientoY(self):
            self.movimientoDerecha = False
            self.movimientoIzquierda = False
            self.cutderecha = False
            self.cutIzquierda = False
            self.respuesta = ""

            def movimientoY(self):
                print("Y turno:")
                x=(input("Entra el numero fila:"))
                y=(input("Entra el numero columna:"))
                if(str(Matrix[x][y])=="O"):
                    if(not y ==7 and not y==0):
                        if(str(Matrix[x-1][y+1])==" "):
                            self.movimientoDerecha=True
                        if(str(Matrix[x-1][y-1])==" "):
                            self.movimientoIzquierda=True
                    elif(y==7):
                        if(str(Matrix[x-1][y-1])==" "):
                            self.movimientoIzquierda=True
                    else:
                        if(str(Matrix[x-1][y+1])==" "):
                            self.movimientoDerecha=True
                    if(not  y>5 and y<2):
                        if(str(Matrix[x-1][y+1])=="X"and not str(Matrix[x-2][y+2])=="X" and not str(Matrix[x-2][y+2])=="O"):
                            self.cutderecha=True
                        if(str(Matrix[x-1][y-1])=="X"and not str(Matrix[x-2][y-2])=="X"and not  str(Matrix[x-2][y-2])=="O"):
                            self.cutIzquierda=True
                    elif(y>5):
                        if(str(Matrix[x-1][y+1])=="X" and not str(Matrix[x-2][y-2])=="X" and  not str(Matrix[x-2][y-2]=="O")):
                            self.cutIzquierda=True
                    else:
                        if(str(Matrix[x-1][y+1])=="X"and not str(Matrix[x-2][y+2])=="X" and not str(Matrix[x-2][y+2])=="O"):
                            self.cutderecha=True
                    if(any([self.cutIzquierda,self.cutderecha])):
                        self.movimientoIzquierda=False
                        self.movimientoDerecha=False
                    if(any([self.movimientoIzquierda,self.movimientoDerecha])):
                        if(self.movimientoIzquierda):
                            if(self.movimientoDerecha):
                                self.respuesta=input("Movimiento Derecha o Izquierda ?, Si es Derecha o Izquierda , si es Derecha responder con D y si es Izquierda con I ")
                                self.respuesta=self.respuesta.upper()
                            else:
                                self.respuesta="I"
                        else:
                            self.respuesta="D"
                    if(any([self.respuesta=="D",self.respuesta=="I"])):
                        if(self.respuesta=="D"):
                            Matrix[x-1][y+1]="O"
                            Matrix[x][y]=" "
                            p.printMatrix(Matrix)
                        else:
                            Matrix[x-1][y-1]="O"
                            Matrix[x][y]=" "
                            p.printMatrix(Matrix)
                    elif(any([self.cutIzquierda,self.cutderecha])):
                        if(self.cutIzquierda):
                            if(self.cutderecha):
                                self.respuesta=input("")
                                self.respuesta=self.respuesta.upper()
                            else:
                                self.respuesta="I"
                        else:
                            self.respuesta="D"
                        if(any([self.respuesta=="D",self.respuesta=="I"])):
                            if(self.respuesta=="D"):
                                Matrix[x-1][y+1]=" "
                                Matrix[x-2][y+2]="O"
                                Matrix[x][y]=" "
                                p.printMatrix(Matrix)
                            else:
                                Matrix[x-1][y-1]=" "
                                Matrix[x-2][y-2]="O"
                                Matrix[x][y]=" "
                                p.printMatrix(Matrix)
                        if(not  y >5 and not y <2):
                            if(str(Matrix[x-1][y+1])=="X"):
