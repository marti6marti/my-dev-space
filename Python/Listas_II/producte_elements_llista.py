from functools import reduce
numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
product = reduce(lambda x, y: x * y, numbers)
print("Producte de tots els elements:", product)
