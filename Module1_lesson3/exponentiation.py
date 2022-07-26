def calculateExponent():
    # Exponentiation Calculator
    print("Exponentiation Calculator")
   

    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    if y == 0:
        return 1
    
    x = x**y
    return x

print(calculateExponent())
