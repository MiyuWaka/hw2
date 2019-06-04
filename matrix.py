import numpy, sys, time

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
a = numpy.zeros((n, n)) # Matrix A
b = numpy.zeros((n, n)) # Matrix B
c = numpy.zeros((n, n)) # Matrix C

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0

#print(a)

begin = time.time()

######################################################
# Write code to calculate C = A * B                  #
# (without using numpy librarlies e.g., numpy.dot()) #
'''
numpy使うと
c = numpy.dot(a, b)
print(c)
'''

import sys

def mul_matrix(a, b):
    n = len(a)
    m = len(b)
    l = len(b[0])
    
    ans = []

    for i in range(n):
        new_row = []
        for j in range(l):
            sum = 0
            for k in range(m):
                sum += a[i][k] * b[k][j]

            new_row.append(int(sum))

        ans.append(new_row)
    
    return ans

c = mul_matrix(a,b)
print(c)
######################################################

end = time.time()
print("time: %.6f sec" % (end - begin))

# Print C for debugging. Comment out the print before measuring the execution time.
total = 0
for i in range(n):
    for j in range(n):
        # print c[i, j]
        total += c[i][j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
print("sum: %.6f" % total)