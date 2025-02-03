list1 = [int(x) for x in input("Introdueix la primera llista de números separats per espais: ").split()]
list2 = [int(x) for x in input("Introdueix la segona llista de números separats per espais: ").split()]
intersection = [x for x in list1 if x in list2]
print("Intersecció:", intersection)
