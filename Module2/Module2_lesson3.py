#Generate and print a dictionary containing keys ranging from 5 to 15 (with both numbers included) and the values are the squares of the keys.

squares = {}
for x in range(5,16):
    squares[x] = x*x

print(squares)    

#Dictionary comprehension
square ={x: x*x for x in range(5,16)}
print(square)