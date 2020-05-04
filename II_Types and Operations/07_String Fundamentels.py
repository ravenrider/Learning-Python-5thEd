##################################################
#literals
##################################################
s = 'Single quotes can contain "doubles"'
s = "Double quotes can contain 'singles'"
title = "Meaning " 'of' " Life" #mixing possible automatic concats
print(title)

#Escape characters
#\\                 Backslash (\)
# \'                Single quote (stores ')
# \"                Double quote (stores ")
# \a                Bell
# \b                Backspace
# \f                Formfeed
# \n                Newline (linefeed)
# \r                Carriage return
# \t                Horizontal tab
# \v                Vertical tab
# \xhh              Character with hex value hh (exactly 2 digits)
# \ooo              Character with octal value ooo (up to 3 digits)
# \0                Null: binary 0 character (doesn’t end string)
# \N                { id }Unicode database ID
# \uhhhh            Unicode character with 16-bit hex value
# \Uhhhhhhhh        Unicode character with 32-bit hex value

#Raw strings ignore escape characters
s = r'C:\new\text.dat'
print(s)
#Raw string can't end with \
s = r'C:\new\text.dat' '\\'
print(s)

#Multiline Block Strings
mantra = """Always look...   
on the bright... 
side of life."""
print(mantra)

##################################################
#In action
##################################################
i = len('abc')      #length of the string
s = 'abc' + 'def'   #Concat
s= 'Ni!' * 4        #Repeat string 4 times Ni!Ni!Ni!Ni!

myjob = 'hacker'
for c in myjob: #Loop all characters
    print(c, end=' ')
print()
#Slicing
S = 'spam'
print(S[0]) #character s
print(S[-2]) #character a (counting backwards)
print(S[1:3]) #Character 1 and 2
print(S[1:]) #All characters from index 1
print(S[:-1]) #All characters except the last one

#Extended slicing lets you skip items with a step
S = 'abcdefghijklmnop'
print(S[1:10:2]) #skip c and e and ...

S = 'hello'
print(S[::-1]) #Reverse string)

#convert int to string
i = 42
s = str(i)
#convert string to number
i = int(s)
r = float(s)

#ordinal
i = ord('s')    #Converts to ascii code
c = chr(i)      #Converts from ascii code

#You can't change 1 character in a string (immutable)

##################################################
#Methods
##################################################
S = S.replace('mm', 'xx')# Replace all mm with xx in 
S.replace('SPAM', 'EGGS', 1)# Replace on

where = S.find('SPAM') # Search for position , -1 if not found
'Ni' in S    #Alternative if you don't need the index

L = list(S) #Creates list of characters, usefull to replace in place
S = ''.join(L) #Implode list back to a string

line = 'bob,hacker,40'
line.split(',') #Creates a list splitted by the choosen delimeter

line = "The knights who say Ni!\n"
line.rstrip() #Strip whitespace at the end
line.upper() #Convert to upper characters
line.isalpha() #returns “True” if all characters in the string are alphabets
line.endswith('Ni!\n')
line.startswith('The')

##################################################
#Formatting
##################################################
'%d %s %g you' % (1, 'spam', 4.0)
# %s string
# %d decimal
# %i integer
# %o Octal
# %x Hex
# %f Floating point
# %06d zerro padding
# %−6.2f Max 6 characters and 2 precision
# %.2 2 precision

#Dictionay based formatting
'%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'}

#Method based
template = '{0}, {1} and {2}'.format('spam', 'ham', 'eggs')
template = '{motto}, {pork} and {food}'.format(motto='spam', pork='ham', food='eggs')

template = '%s, %s and %s'
template % ('spam', 'ham', 'eggs')

template = '%(motto)s, %(pork)s and %(food)s'
template % dict(motto='spam', pork='ham', food='eggs')

import sys
s = 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})

#Advanced formatting methods
'{0:10} = {1:10}'.format('spam', 123.4567) #10 chars aligned left
# 'spam       =   123.4567

'{0:>10} = {1:<10}'.format('spam', 123.4567) #10 chars aligned right

#All above is also possible in expression
'%10s = %-10s' % ('spam', 123.4567)
'%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop')

#New option since version 3.6 is a formatting string
shepherd = 'Jan'
age = 18
s = f"Shepherd {shepherd} is {age} years old."
