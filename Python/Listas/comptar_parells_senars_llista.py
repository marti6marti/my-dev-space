numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
even_count = sum(1 for x in numbers if x % 2 == 0)
odd_count = sum(1 for x in numbers if x % 2 != 0)
print("Parells:", even_count)
print("Senars:", odd_count)
