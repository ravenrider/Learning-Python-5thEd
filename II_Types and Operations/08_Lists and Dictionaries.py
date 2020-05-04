##################################################
#Lists In action
##################################################
i = len([1, 2, 3]) #Length = 3
[1, 2, 3] + [4, 5, 6] # Concat = [1, 2, 3, 4, 5, 6]

res =[c * 4 for c in 'SPAM'] # ['SSSS', 'PPPP', 'AAAA', 'MMMM']
# same as
#res = []
#for c in 'SPAM':
#   res.append(c * 4)

#Mapping a function to a list
list(map(abs, [-1, -2, 0, 1, 2]))# Map a function across a sequence --> [1, 2, 0, 1, 2]

#Slicing and indexing same as strings
L = ['spam', 'Spam', 'SPAM!']
L[2]# Offsets start at zero
L[-2]# Negative: count from the right
L[1:]# Slicing fetches sections

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[2][0]

L[0:2] = ['eat', 'more'] #Only change index 0 and 1, rest of the list stays unchanged
L = [1, 2, 3]
L[1:2] = [4, 5] #First remove index 1 and then insert 4 and 5 ==> [1, 4, 5, 3]
L[1:1] = [6, 7] # Insertion (replace nothing) ==> [1, 6, 7, 4, 5, 3]
L[1:2] = []# Deletion (insert nothing) ==> [1, 7, 4, 5, 3]

##################################################
#Lists Methods
##################################################
#append and sort change the associated list object inplace, but don’t return the list as a result
L = []
L.append('please')# Append method call: add item at end
L.insert(0, 'please')  #Insert method call: add item at index

L.sort()# Sort list items 
L.sort(key=str.lower) # Normalize to lowercase before sorting
L.sort(key=str.lower, reverse=True)# Change sort orde

#If you want a new list then you have to use built-in sorting
sorted(L, key=str.lower, reverse=True)

L.extend([3, 4, 5])# Add many items at end (like in-place +
L.pop()# Delete and return last item (by default: −1
L.pop(1)# Delete item at index 1
L.reverse()# In-place reversal method
L.index('please')# Index of an object (search/find)
L.remove('please')# Delete by value
L.count('spam')# Number of occurrences
T = L.copy() #Copy list

##################################################
#Dictionaries in Action
##################################################
D = {'spam': 2, 'ham': 1, 'eggs': 3}# Make a dictionary
D = dict(name='Bob', age=40)               # dict keyword argument form
D = dict([('name', 'Bob'), ('age', 40)]) # Make a dictionary
#dict(zip(keyslist, valueslist)) #Create from lists

# Fetch a value by key, this can give an error if it does not exist
o = D['spam']
# Solution Get, if not found return None
o = D.get('spam')

# Add new entry
D['brunch'] = 'Bacon'
#Better use update to update and insert values
D2 = {'toast':4, 'muffin':5}
D.update(D2)

#Delete entry
del D['eggs']# Delete entry
#Better use pop in case no key is there
D.pop('toast')# Delete and return from a key

len(D)# Number of entries in dictionary
'ham' in D # Key membership test alternative True or False
list(D.keys())# Create a new list of D's keys
list(D.values()) # Create a new list of D's values
list(D.items()) # Create a new list of D's items like [('eggs', 3), ('spam', 2), ('ham', 1)]

#Dictionary and yo uwant a value from a key
table = {
'1975': 'Holy Grail',
'1979': 'Life of Brian',
'1983': 'The Meaning of Life'
}
for year in table:
    print(year + '\t' + table[year])

#Dictionary where you know the value but need the key
table = {
'Holy Grail':'1975',
'Life of Brian':'1979',
'The Meaning of Life': '1983'
}
Movie = [title for (title, year) in table.items() if year == '1975']
print(Movie)

#You can use dictionaries as lists but you don't need to allocate all the memory for maybe empty positions
D = [0] * 100
#If you aonly need a few index you can use
D = {}
D[95] = 20
#Or if you need a matrix you can use tuples (immutable) to declare them
Matrix = {}
Matrix[(2, 3, 4)] = 88



