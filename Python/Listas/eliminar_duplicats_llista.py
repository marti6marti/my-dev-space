numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
unique_numbers = list(dict.fromkeys(numbers))
print("Llista sense duplicats:", unique_numbers)
