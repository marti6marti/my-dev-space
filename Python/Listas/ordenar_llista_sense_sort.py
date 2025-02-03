numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Llista ordenada:", numbers)
