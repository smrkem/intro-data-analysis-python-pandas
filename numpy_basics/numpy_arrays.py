import numpy as np


# numpy arrays vs. python lists
py_list = [1, 2, 3]
py_list_2 = [4, 5, 6]

# now add them together, the '+' operator concatenates them
py_list_sum = py_list + py_list_2
print(py_list_sum)

# Create a numpy array from the python lists
np_array = np.array(py_list)
np_array_2 = np.array(py_list_2)

# add them. The '+' operator performs element-wise addition:
np_array_sum = np_array + np_array_2
print(np_array_sum)

# Try to perform an operation like '*' on a list
product_list = py_list * 5
print(product_list)

# But no problem on an array
print(np_array * 5)

# numpy arrays handles multidimensional arrays easily
py_multidim_list = [
    [1,2], [4,5], [5,6]
]
np_multidim_list = np.array(py_multidim_list)
print(np_multidim_list)

# and numpy has several nice helper methods for working with arrays
print(np_multidim_list.shape, np_multidim_list.ndim, np_multidim_list.size)

# can access a multidim array like lists:
print(np_multidim_list[0][1])

# but also in a tuple syntax
print(np_multidim_list[0,1])

# and also use ranges
print(np_multidim_list[1:,1])

# passing a boolean in the square brackets gives a mask for picking out values:
print(np_multidim_list < 5)
print(np_multidim_list[np_multidim_list < 5])

# note positional information gets lost
print(np_multidim_list[np_multidim_list < 50])

# numpy arrays can only contain a single data type,
# and will type cast as necessary to convert
py_list_3 = [1, True, 'False', 13.05]
np_array_3 = np.array(py_list_3)
print(np_array_3)

