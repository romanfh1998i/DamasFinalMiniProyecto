


class matrix:

    def printMatrix(self, Matrix):
        print("\n\n")
        print("------------------Damas_Cinncinatus-----------")
        print("\n")
        print("0 |  1  |  2  |  3  |  4  |  5  |  6  |  7 \n")
        print("--------------------------------------------")
        for fila in Matrix:
            print("  |  ".join(map(str, fila)))
            print("-------------------------------------------")
        print("\n")
        print("")
        print("\n\n")


# aqui se instancia el tablero osea que se hace un llamado de la funcion de arriba  que donde se imprime el tablero

Matrix = [[]]
Matrix = [[' ' for x in range(8)] for y in range(8)]
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















