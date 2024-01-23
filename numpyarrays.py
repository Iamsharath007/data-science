import numpy as np

# Some basic array functions
np_array = np.arange(1, 11, 1)  # start , stop , step
print(np_array)

np_array = np.linspace(1, 10, 6)  # start, stop , number of elements
print(np_array)

print(np.zeros((3, 6)))  # row , column
print(np.zeros((3, 6)).shape)

print(np_array.reshape((2, 3)))
print(np_array.ravel())

# Some mathematical fucnitons
np_array = np_array.reshape((3, 2))
print(np_array.min())  # can also use max
print(np_array.sum(axis=0))  # column wise sum
print(np_array.sum(axis=1))  # row wise sum
print(np.std(np_array))  # standard deviation

a = np.zeros((2, 2))
b = np.ones((2, 2))
print(a + b + 3)
print(a.dot(b))  # dot product

for cell in a.flat:
    print(cell)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

print(b >= 1)
