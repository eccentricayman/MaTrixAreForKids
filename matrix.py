import math


def print_matrix( matrix ):
    retStr = "";
    for i in range(len(matrix)):
        #print the left border
        retStr += "|"
        #print the row, except for the last number
        for j in range(len(matrix[i]) - 1):
            retStr += str(matrix[i][j]) + "\t"
        #print last number without tab
        retStr += str(matrix[i][j])
        #print right border with newline
        retStr += "|\n"
    #get rid of last newline
    print retStr[:-1]
    
def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

print_matrix(new_matrix())
