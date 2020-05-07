#Any object witha __next__ method to advance to a next result, which raises StopIteration at the end
#of the series of results, is considered an iterator in Python
#for some objects the full protocol includes an additional first step to call iter, but this isn’t required forfiles.

import os
import sys

for line in open(os.path.join(sys.path[0],'13_Loops.py')):# Use file iterators to read by lines...    
     print(line.upper(), end='')

#same as manual
f = open(os.path.join(sys.path[0],'13_Loops.py'))
print(next(f))# The next(f) built-in calls f.__next__() 
next(f)

#Initial step before iteration (not required for files)
L = [1, 2, 3]
I=iter(L)
print(next(I))

# Manual iteration: what for loops usually do'
I = iter(L)
while True:
    try:# try statement catches exceptions...         
        X = next(I)# Or call I.__next__ in 3.X...     
    except StopIteration:
        break
    print(X ** 2, end=' ')

#Dictionaries return key in an iterantion next
D = {'a':1, 'b':2, 'c':3}
for key in D:
    print(key, D[key])

##################################
#List Comprehensions
##################################
for i in range(len(L)):
    L[i] += 10
#Better solution
L = [x + 10 for x in L]

#on files
lines = [line.rstrip() for line in open(os.path.join(sys.path[0],'13_Loops.py'))]

#Filters
lines = [line.rstrip() for line in open(os.path.join(sys.path[0],'13_Loops.py')) if line[0] == 'p']