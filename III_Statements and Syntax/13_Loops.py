#break          Jumps out of the closest enclosing loop (past the entire loop statement)
#continue       Jumps to the top of the closest enclosing loop (to the loop’s header line)
#pass           Does nothing at all: it’s an empty statement placeholderLoop 
#else block     Runs if and only if the loop is exited normally (i.e., without hitting a break)
y = 5
x = y // 2                                
while x > 1:    
    if y % x == 0:                        # Remainder        
        print(y, 'has factor', x)        
        break                             # Skip 
    x -= 1
else:                                     # Normal exit    
    print(y, 'is prime')

#For is faster than while
#If you need an index you can use the range function
#list(range(5, −5, −1))
#[5, 4, 3, 2, 1, 0, −1, −2, −3, −4]

#Zipping
T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
list(zip(T1, T2, T3))
#[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#Use zips to create dictionaries from lists
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
list(zip(keys, vals))
D2 = {}
#for (k, v) in zip(keys, vals): D2[k] = v   #OLD WAY
D3 = dict(zip(keys, vals))                  #NEW WAY

#Using object AND index
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

