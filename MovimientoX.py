from Matrix import Matrix
from Matrix import matrix
p=matrix()

class Jugador1:
    def variable(self,movimientoDerecha,movimientoIzquierda,cutderecha,cutizquierda):
        self.x=[]
        self.y=[]
        self.respuesta=[]
        self.movimientoDerecha=movimientoDerecha
        self.movimientoIzquierda=movimientoIzquierda
        self.cutderecha=cutderecha
        self.cutizquierda=cutizquierda
    def movimientoJ1(self):
            self.movimientoDerecha=False
            self.movimientoIzquierda=False
            self.cutderecha=False
            self.cutizquierda=False
            respuesta=" "
            print("X turno ")
            x = int(input("Entra el numero fila:"))
            y = int(input("Entra el numero columna:"))
            if (str(Matrix[x][y]) == "X"):
                if (not y == 7 and not y == 0):

                    if (str(Matrix[x + 1][y + 1]) == " "):
                        self.movimientoIzquierda = True
                    if (str(Matrix[x + 1][y - 1]) == " "):
                        self.movimientoIzquierda = True
                elif (y == 7):
                        if (str(Matrix[x + 1][y - 1]) == " "):
                            self.movimientoDerecha = True
                else:
                    if (str(Matrix[x + 1][y + 1]) == " "):
                            self.movimientoDerecha = True
                if (not y > 5 and not y < 2):
                        if (str(Matrix[x + 1][y + 1]) == "O" and not str(Matrix[x + 2][y + 2]) == "O" and not str(
                                Matrix[x + 2][y + 2]) == "X"):
                            self.cutderecha = True
                        if (str(Matrix[x + 1][y - 1]) == "O" and not str(Matrix[x + 2][y - 2]) and not str(
                                Matrix[x + 2][y - 2]) == "X"):
                            self.cutizquierda = True
                elif(y>5):
                        if(str(Matrix[x+1][y+1])=="O"and not str(Matrix[x+2][y+2])=="O"and not str(Matrix[x+2][y-2])=="X"):
                            self.cutizquierda=True
                else:
                        if(str(Matrix[x+1][y+1])=="O"and not str(Matrix[x+2][x-2])=="O"and not str(Matrix[x+2][y+2])=="X"):
                            self.cutderecha=True
                if(any([self.cutizquierda,self.cutderecha])):
                    self.movimientoIzquierda=False
                    self.movimientoDerecha=False
                if(any([self.movimientoIzquierda,self.movimientoDerecha])):
                    if(self.movimientoIzquierda):
                        if(self.movimientoDerecha):
                            respuesta=input("Movimiento Derecha o Izquierda ?, Si es Derecha o Izquierda , si es Derecha responder con D y si es Izquierda con I")
                            respuesta=respuesta.upper()
                        else:
                            respuesta="I"
                    else:
                        respuesta="D"
                if(any([respuesta=="D",respuesta=="I"])):
                        if(respuesta=="D"):
                            Matrix[x+1][y+1]="x"
                            Matrix[x][y]=" "
                            p.printMatrix(Matrix)
                        else:
                            Matrix[x+1][y-1]="x"
                            Matrix[x][y]=" "
                            p.printMatrix(Matrix)
                        if(any([respuesta=="D",respuesta=="I"])):
                            if(respuesta=="D"):
                                Matrix[x+1][y+1]=" "
                                Matrix[x][y]="x"
                                p.printMatrix(Matrix)
                            else:
                                Matrix[x+1][y-1]=" "
                                Matrix[x][y]="x"
                                p.printMatrix(Matrix)
                        elif(any([self.cutizquierda,self.cutderecha])):
                            if(self.cutizquierda):
                                if(self.cutderecha):
                                    respuesta=input("Movimiento Derecha o Izquierda,si es Derecha responder con D y si es Izquierda con I")
                                    respuesta=respuesta.upper()
                                else:
                                    respuesta="D"
                            else:
                                respuesta="I"
                        if(any([respuesta=="D",respuesta=="L"])):
                            if(respuesta=="D"):
                                Matrix[x+1][y+1]=" "
                                Matrix[x+2][y+2]="x"
                                Matrix[x][y]=" "
                            else:
                                Matrix[x+1][y-1]=" "
                                Matrix[x+2][y-2]="x"
                                Matrix[x][y]=" "
                                p.printMatrix(Matrix)

                        if(not y>5 and not y<2):
                            if(str(Matrix[x+1][y+1])=="O" and not str(Matrix[x+2][y+2])=="O" and not str(Matrix[x+2][y+2])=="X"):
                                self.cutderecha=True
                            if(str(Matrix[x+1][y-1])=="O"and not str(Matrix[x+2][y-2])=="O" and not str(Matrix[x+2][y-2])=="X"):
                                self.cutizquierda=True
                        elif(y>5):
                            if(str(Matrix[x+1][y-1])=="O"and not str(Matrix[x+2][y-2])=="O" and not str(Matrix[x+2][y-2])=="X"):
                                self.cutderecha=True
                        else:
                            if(str(Matrix[x+1][y+1])=="O" and not str(Matrix[x+2][y+2])=="O" and not str(Matrix[x+2][y+2])=="X"):
                                self.cutizquierda=True


                else:
                        print("Movimiento Invalido")
                        self.movimientoJ1()
            else:
                    print("No es correcto")
                    self.movimientoJ1()
