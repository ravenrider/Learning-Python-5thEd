##################################################
#Tuples In action
##################################################
y = (40,)# A tuple containing an integer, without the comma it will not be a tuple if you only have one item
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)# Make a list from a tuple's item
tmp.sort()
T = tuple(tmp)# Make a tuple from the list's item
sorted(T)# Or use the sorted built-in, and save two step

T = (1, [2, 3], 4)
#T[1] = 'spam'# This fails: can't change tuple itself
T[1][0] = 'spam'# This works: can change mutables inside

T.count(2)# How many 2s are there?
T.index(2, 2)# Offset of appearance after offset 2

##################################################
#NamedTuple In action
##################################################
from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])# Make a generated clas
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])# A named-tuple record

bob[0], bob[2]# Access by position
bob.name, bob.jobs# Access by attribute

O = bob._asdict()# Dictionary-like form
O['name'], O['jobs']# Access by key too

##################################################
#Files In action
##################################################
myfile = open('', 'w') #Default mode is read, 'r' read, 'w' to write, or 'a' to append
myfile.write('hello text file\n')# Write a line of text: string
myfile.close()# Flush output buffers to disk

myfile = open('myfile.txt')# Open for text input: 'r' is defaul
myfile.readline()# Read the lines back
open('myfile.txt').read()# Read all at once into string
for line in open('myfile.txt'):# Use file iterators, not reads...     
    print(line, end='')

data = open('data.bin', 'rb').read() #Read binary files

#Storing Python Objects in Files: Conversions
S = 'Spam'
X, Y, Z = 43, 44, 45
F = open('datafile.txt', 'w')# Create output text file
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.close()
#You can use Eval(readline) to add dictionaries and such back but this can be dangerous since eval excecute evrything as real python code
#And can  execute malicious code, better use pickle
import pickle
D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)

#Store in JSON format
import json
name = dict(first='Bob', last='Smith')
rec  = dict(name=name, job=['dev', 'mgr'], age=40.5)
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4) #Write Json
P = json.load(open('testjson.txt')) #Load Json

#Storing Packed Binary Data: struc
import struct
F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
#we're wanting to pack the data as big-endian (>), 
# var1 as 4-byte integer (i4), 
# var2 as string (s),
# var3 as short integer (h).
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
values = struct.unpack('>i4sh', data)



