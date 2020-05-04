import math
import random

a = 3
b = 4

# add and substract
print(a + 1, a - 1)
#Multiplication and divsion
print(b * 3, b / 2)
#Modulus and power
print(a % 2, b ** 2)
#Integer part division, flooring
print(a // 2)

#Formatting numbers
num = 1 /3
print(num)
print('%e' %num)
print('%.2f' %num)
print('{0:.2f}'.format(num))

# Chained comparisons: range tests
X = 2
Y = 4
Z = 6
print(X < Y < Z)

#Flooring and truncation
# Closest number below value, same as //
print(math.floor(2.5))
print(math.floor(-2.5))
#Closest to 0, same as int()
print(math.trunc(2.5))
print(math.trunc(-2.5))
#Really rounding a number to the closest specified accuracy
print(round(2.567))
print(round(2.567,2))

#oct,hex and binair
#Use them
64, 0o100, 0x40, 0b1000000
print(64,0o100,0x40,0b1000000)
# number to string oct, hex, binair
print(oct(64), hex(64), bin(64))
# string to number
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
#string formatting
print('{0:o}, {1:x}, {2:b}'.format(255, 255, 255)) 

# Complex number also can use method complex(x,y)
print(3.0+4.0j)

#Bitwise Operations
x = 1 # 1 decimal is 0001 in bits
print(x)
y = x << 2# Shift left 2 bits: 0100
print(y)
y = x | 2 # Bitwise OR
print(y)
y = x & 1 # Bitwise AND
print(y)
#X ^ 2  # Bitwise XOR: either but not both

#bit length
X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)

#Constants
print(math.pi)
print(math.e)

#sin,cos,tan
print(math.sin(2))

#absolute value
print(abs(-2))

#min and max
print(min(-5,6,2),max(-10,50,20))

#Square root
print(math.sqrt(144))
print(144 ** 0.5)

#Random
print(random.random()) #Between 0 and 1
print(random.randint(1,10)) #Between 1 and 10 including 1 and 10
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))
suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)


#Decimals
#Fixed precision floats, for example vor currency
from decimal import Decimal
import decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))

#Fraction type
from fractions import Fraction
x = Fraction(4, 6)
print(x)
x = Fraction('.25')
print(x)
#float to fraction
f = 2.5
x = f.as_integer_ratio()
print(x)
x = Fraction.from_float(1.75)
print(x)
#fraction to float
x = float(Fraction(4, 6))
print(x)

#0.33333333333 to fraction ? --> limit denominator
a = 1 / 3
a = Fraction(*a.as_integer_ratio())
print(a)
print(a.limit_denominator(10))

