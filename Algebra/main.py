#!/usr/bin/python
from Matrix import Matrix

a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
b = Matrix([[1,2,3,4,5,6], [10,11,12,13,14,15], [-1,-2,-3,-4,-5,-6]])
c = Matrix([[11,22,33],[44,55,66],[77,88,99]])

print("Matrix B")
b.showMatrix()

print("Matrix A")
a.showMatrix()

print("Transpose A")
a.transpose().showMatrix()

print("A->getRow(1,2,3) = ", a.getRow(1,2,3))
print("A->getColumn(1,2) = ", a.getColumn(1,2))

print("This is Scalar Mult: A * 2")
multTest1 = a*2
multTest1.showMatrix()

print("This is Scalar RMult: 2 * A")
multTest2 = 2*a
multTest2.showMatrix()

print("This is Addition: A+B")
addTest = a + b
addTest.showMatrix()
print("This is Addition: A+C")
addTest = a + c
addTest.showMatrix()
print("This is Substraction: A-C")
addTest = a - c
addTest.showMatrix()


ab = Matrix([[1,2,3],[4,5,6]])
cd = Matrix([[7,8],[9,10],[11,12]])

print("Matrix multiplication")
matMultTest = ab@cd
matMultTest.showMatrix()

testDet = Matrix([[1,2],[3,4]])
testDet = Matrix([[3,8],[4,6]])
print("Determinant of testDet = ", testDet.determinant())

testAdjucate = Matrix([[-3,2,-5],[-1,0,-2],[3,-4,1]])
testAdjucate = Matrix([[0,1,0],[1,5,1],[0,1,0]])
testAdjucate = Matrix([[1,2],[2,-1]])
print("Adjucate test: ")
testAdjucate.adjugate().showMatrix()

testInverse = Matrix([[1,2,3],[3,2,1],[1,0,1]])
testInverse = Matrix([[1,2],[2,-1]])
testInverse = Matrix([[3,8],[4,6]])
print("Inverted Matrix test: ")
testInverse.inverted().showMatrix()

testLast = Matrix([[0,1,0],[1,5,1],[0,1,0]])
testLast.showMatrix()
print("Last Method get part of Matrix")
testLast.getPartOfMatrixFromColumn(3,2,1).showMatrix()
# print("This is Matrix Dot Multiplication: ", a**b)
# print("This is Matrix Cross Multiplication: ", a@b)
