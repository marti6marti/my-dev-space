from itertools import combinations
numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
k = int(input("Introdueix la longitud de les combinacions: "))
combinations_list = list(combinations(numbers, k))
print("Combinacions possibles:", combinations_list)
