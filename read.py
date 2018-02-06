import numpy
a=numpy.zeros((10,20))

file=open('mars.txt','r+')
lines=file.read()
print(lines)
for line in lines:

    a [:]=line[:]
print(a)