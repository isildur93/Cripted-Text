

import numpy
from numpy import linalg as Vector
from lib import *
from string import maketrans
sub = numpy.array(RealFrequency)
intab = alfaString
Results=[]
for keyIndex in range(0,26):
    lista =[]
    sh = shift(list(alfaString),keyIndex)
    outtab = ''.join(sh)
    trantab = maketrans(intab, outtab)
    decoded = encoded.translate(trantab)
    for char in list(alfaString):

        num = decoded.count(char)
        lista.append((num*100) / 275 )


    n = numpy.array(lista)
    Difference = n-sub
    result = Vector.norm(Difference)
    Results.append(result)

    del lista



m=min(Results)
index = Results.index(m)
with open('Solution.txt', 'w') as f:
    f.write('The key solution is   {} \n \n  '.format(index))
    sh = shift(list(alfaString),index)
    outtab = ''.join(sh)
    trantab = maketrans(intab, outtab)
    decoded = encoded.translate(trantab)
    f.write(str(decoded))
    f.close()
