#########################
#Unpacking
#########################
# The variable with the star takes all the remaining items in a list
a, *b, c = range(4) 
#a, b, c
#(0, [1, 2], 3)

#If only one item it is still a list
seq = [1, 2, 3, 4]
a, b, c, *d = seq
#print(a, b, c, d)
#1 2 3 [4]

#If no items are left to unpack the starred item is an empty list
a, b, c, d, *e = seq
#print(a, b, c, d, e)
#1 2 3 4 []

#########################
#Multitarget
#########################
a = b = c = 'spam'

#########################
#Augmented assignment
#########################
x=0
x = x + 1
x += 1

L = [1, 2]
L = L + [3]# Concatenate: slower
L.append(4)# Faster, but in place

#########################
#Naming conventions
#########################
#Names that begin with a single underscore (_X) are not imported by a from module import * statement
#Names that have two leading and trailing underscores (__X__) are system-definednames that have special meaning to the interpreter.
#Names that begin with two underscores and do not end with two more (__X) are localized (“mangled”) to enclosing classes (see the discussion of pseudoprivateattributes in Chapter 31).
#The name that is just a single underscore (_) retains the result of the last expressionwhen you are working interactively.

#########################
#Print
#########################
#print([object, ...][, sep=' '][, end='\n'][, file=sys.stdout][, flush=False])
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='...', end='!\n')

#EASY WAY
#Using a different file to output the print
#print(x, y, z, sep='...', file=open('data.txt', 'w'))

#HARD WAY
import sys
temp = sys.stdout# Save for restoring late
#sys.stdout = open('log.txt', 'a')       # Redirects prints to a file...
#print(x, y, x)                          # Shows up in log.txt
#sys.stdout.close()# Flush output to disk

#Print to the error stream
print('Bad!' * 8, file=sys.stderr)