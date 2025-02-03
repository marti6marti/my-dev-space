numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
rotations = int(input("Introdueix el nombre de rotacions: "))
rotated_list = numbers[rotations % len(numbers):] + numbers[:rotations % len(numbers)]
print("Llista rotada:", rotated_list)
