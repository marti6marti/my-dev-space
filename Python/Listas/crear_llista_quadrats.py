numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
squared_numbers = [x**2 for x in numbers]
print("Llista de quadrats:", squared_numbers)
