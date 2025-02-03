numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
filtered_list = [x for x in numbers if numbers.count(x) % 2 == 0]
print("Llista filtrada:", filtered_list)
