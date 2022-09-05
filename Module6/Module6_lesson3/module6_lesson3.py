import numpy as np
# print("imported successfully")

#The array of numbers between 1 and 100
list = [*range(1, 101)]
# print(list)

#To generate the even numbers within the array
even_number = np.array([*filter(lambda x: x%2 == 0, list)])
# print(even_number)

#To generate the lcm of the even numbers
lcm = np.lcm.reduce(even_number)
# print(lcm)