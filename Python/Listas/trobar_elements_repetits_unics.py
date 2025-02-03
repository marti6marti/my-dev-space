numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
unique_repeated = set(x for x in numbers if numbers.count(x) > 1)
print("Elements repetits únics:", list(unique_repeated))
