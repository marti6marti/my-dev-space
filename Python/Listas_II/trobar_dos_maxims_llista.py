numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
largest = second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Dos nombres més grans:", largest, second_largest)
