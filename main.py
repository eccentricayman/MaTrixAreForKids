from display import *
from draw import *
import math
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "printin matrix"
print_matrix(matrix)

print "new matrix"
imatrix = new_matrix()
print_matrix(imatrix)

print "* 2"
scalar_mult(imatrix, 2)
print_matrix(imatrix)

print "making to identity matrix"
ident(imatrix)
print_matrix(imatrix)

print "matrix * imatrix"
matrix_mult(imatrix, matrix)
print_matrix(matrix)

print "adding stuff 2 matrix"
for i in range(500):
    add_edge(matrix, int(math.sin(i / (2 * math.pi))) * i, int(math.cos(i / (2 * math.pi))) * i, 0, int(math.tan(i / (2 * math.pi))) * i, int(math.atan(i / (2 * math.pi))) * i, 0)

draw_lines( matrix, screen, color )
display(screen)
