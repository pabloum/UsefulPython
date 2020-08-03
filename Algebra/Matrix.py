from Vector import *

class Matrix():

    def __init__(self, matrix):
        self.validMatrix = True
        self.matrix  = matrix
        try:
            self.rows    = len(matrix)
            self.columns = len(matrix[0])
        except IndexError:
            self.rows    = 0
            self.columns = 0
            self.validMatrix = False

        for i in range(self.rows):
            if len(matrix[i]) != self.columns:
                self.validMatrix = False
                self.matrix = []

    def isValidMatrix(self):
        return self.validMatrix

    def showMatrix(self):
        if self.validMatrix:
            for i in range(self.rows):
                for j in range(self.columns):
                    print(self.matrix[i][j], end="\t")
                print()
        else:
            print("Your matrix is invalid or empty")

    def dimensions(self):
        return [self.rows, self.columns]

    #Matrices addition
    def __add__(self, mat):
        if self.validMatrix and self.dimensions() == mat.dimensions():
            result = []
            for i in range(self.rows):
                result.append([])
                for j in range(self.columns):
                    result[i].append(self.matrix[i][j] + mat.matrix[i][j])
            return Matrix(result)
        else:
            return Matrix([])

    #Matrices substraction
    def __sub__(self, mat):
        return self  + mat*(-1)

    #scalar multiplication
    def __mul__(self, scalar):
        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.columns):
                result[i].append(self.matrix[i][j] * scalar)
        return Matrix(result)

    def __rmul__(self, scalar):
        return self * scalar

    #Matrices multiplication
    def __matmul__(self,mat):
        if self.columns == mat.rows:
            result = []
            for i in range(self.rows):
                row = []
                for j in range(mat.columns):
                    rowA = self.getRow(i)[0]
                    colB = mat.getColumn(j)[0]
                    component = Vector(rowA) * Vector(colB) # Dot product
                    row.append(component)
                result.append(row)
        return Matrix(result)

    def transpose(self):
        if self.validMatrix:
            transposedMatrix = [self.getColumn(n)[0] for n in range(self.columns)]
            return Matrix(transposedMatrix)
        else:
            return Matrix([])

    def getCofactor(self, rowToBeIgnored, colToBeIgnored):
        small = []
        for i in range(0, self.rows):
            if i is rowToBeIgnored: continue
            row = []
            for j in range (self.columns):
                if j is colToBeIgnored: continue
                row.append(self.matrix[i][j])
            small.append(row)
        return Matrix(small)

    def determinant(self):
        if self.validMatrix and self.columns is self.rows:
            if self.dimensions() == [1, 1]:
                det = self.matrix[0][0]
            else:
                sign = 1
                det  = 0
                for col in range(self.columns):
                    det += sign * self.matrix[0][col] * self.getCofactor(0,col).determinant()
                    sign *= -1
            return det
        else:
            return None

    def adjugate(self):
        cofactorMatrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                component = (-1)**(i+j) * self.getCofactor(i,j).determinant()
                row.append(component)
            cofactorMatrix.append(row)
        cofactorMatrix  = Matrix(cofactorMatrix)
        adjugatedMatrix = cofactorMatrix.transpose()
        return adjugatedMatrix

    def inverted(self):
        inverted = (self.adjugate())*(1/self.determinant())
        return inverted

    def getRow(self, *rows):
        if self.validMatrix:
            lst = []
            for i in rows:
                if i >= self.rows: break #Avoids searching the column if the index is greater than max row
                lst.append(self.matrix[i])
            return lst
        else:
            return None

    def getColumn(self, *columns):
        if self.validMatrix:
            lst = []
            for column in columns:
                if column >= self.columns: break #Avoids searching the column if the index is greater than max column
                asked_column = []
                for i in range(self.rows):
                    for j in range(self.columns):
                        if j is column:
                            asked_column.append(self.matrix[i][j])
                            break
                lst.append(asked_column)
            return lst
        else:
            return None

    def getPartOfMatrixFromColumn(self,rows,columns,from_):
        result = []
        for i in range(rows):
            row = []
            for j in range(from_, from_ + columns):
                row.append(self.matrix[i][j])
            result.append(row)
        return Matrix(result)
