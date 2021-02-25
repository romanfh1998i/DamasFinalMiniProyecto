from Matrix import Matrix
from Matrix import matrix
p=matrix()
p.printMatrix(Matrix)
class MovimientoY:
    def variable(self,movimientoDerecha,movimientoIzquierda,cutderecha,cutizquierda):
        self.x=[]
        self.y=[]
        self.respuesta=[]
        self.movimientoDerecha=movimientoDerecha
        self.movimientoIzquierda=movimientoIzquierda
        self.cutderecha=cutderecha
        self.cutizquierda=cutizquierda
    def MovimientoJ2(self):
        self.movimientoDerecha=False
        self.movimientoIzquierda=False
        self.cutizquierda=False
        self.cutderecha=False

