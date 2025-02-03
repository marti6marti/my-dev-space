numbers = [int(x) for x in input("Introdueix una llista de números separats per espais: ").split()]
subsequences = []
current_subsequence = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1] + 1:
        current_subsequence.append(numbers[i])
    else:
        subsequences.append(current_subsequence)
        current_subsequence = [numbers[i]]
subsequences.append(current_subsequence)
print("Subseqüències consecutives:", subsequences)
