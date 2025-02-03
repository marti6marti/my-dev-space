numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
positive_sum = sum(x for x in numbers if x > 0)
print("Suma de positius:", positive_sum)
