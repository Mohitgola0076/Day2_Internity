''' The slice() function returns a slice object.
A slice object is used to specify how to slice a sequence. We can specify where to start the slicing, and where to end. 
We can also specify the step, which allows us to e.g. slice only every other item. 
Syntax:-
slice(start, end, step)
'''

# 1.)   Print in given range 
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
          # It will print output from index (3) to index (4) only two words.
 
# 2.)   slicing with jump in given range.
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])
         # It will print from starting to 7th index with jump of two index
  
# 3.)   Get substring using slice object
# Program to get a substring from the given string 

py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3) 
print(py_string[slice_object])  

# Output:  Pyt

# 4.)   Get substring using negative index

py_string = 'Python'

# start = -1, stop = -4, step = -1
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)

print(py_string[slice_object]) 
# Output :   noh


# 5.)  Get sublist and sub-tuple using slicing

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h')    

# output : 
['P', 'y', 't']
('y', 'h')



