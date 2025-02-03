list1 = [int(x) for x in input("Introdueix la primera llista de números separats per espais: ").split()]
list2 = [int(x) for x in input("Introdueix la segona llista de números separats per espais: ").split()]
combined = list(zip(list1, list2))
print("Llista combinada:", combined)
