#import numpy
import numpy as np
print("imported successfully")

#Creating a list of integers between numbers from 5.5 to 20.5
number = [int(i) for i in np.arange(5.5, 21.5)]
print([*(number)])

#The count of odd numbers in the list 
odd_number = [*filter(lambda i: (i%2 != 0), number)]
print(len(odd_number))

#The count of even numbers in the list 
even_number =[*filter(lambda i: (i%2 == 0), number)]
print(len(even_number))

# square of every number in the list
square = [*map(lambda x: (x**2), number)]
print(square)

#cube of every number in the list
cube = [*map(lambda x: (x**3), number)]
print(cube)
