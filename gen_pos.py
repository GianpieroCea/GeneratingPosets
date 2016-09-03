#program POSET

# A python implementation of the algorithm at
# http://www.jstor.org/stable/pdf/2686806.pdf to generate posets

max_val = 3 #constant
matrix =  [[False for x in range(max_val)] for y in range(max_val)]

def getB(relations):
    '''
    input: a list <relations> consisting of a pair of coordinates for
            determining the order relation

    output: a matrix B that represents the order relation
    '''
    B = [[False for x in range(max_val)] for y in range(max_val)]
    for relation in relations:
        B[relation[0]][relation[1]] = True
    return B

def print_m(matrix):
    '''
    input: a bidimensional array <matrix>
    output: prints it
    '''
    for row in matrix:
        print (row)

def generate(B):
    '''
    input: a bidimensional array <B> representing the partial order
    output: a new matrix <A> obtained by transitivity
    '''
    consistent = True
    j= 0
    while(consistent and j< max_val):
        j=j+1
        for i in range(1,max_val+1):
            if B[i-1][j-1]:
                for k in range(1,max_val+1):
                    B[i-1][k-1]= B[i-1][k-1] or B[j-1][k-1]
        consistent = not B[j-1][j-1]
    ok = consistent
    return [B,ok]


if __name__ == "__main__":
    #just an example,change here
    relations = [[0,1],[1,2]]
    B = getB(relations)
    print('The generating matrix is:')
    print_m(B)
    [A,ok]= generate(B)
    if not ok:
        print('Inconsinstent')
    else:
        print('The poset matrix is:')
        print_m(A)
