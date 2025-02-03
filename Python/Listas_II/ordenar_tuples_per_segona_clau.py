tuples = [tuple(input("Introdueix un tuple (element1, element2) separat per coma: ").split(',')) for _ in range(int(input("Quants tuples? ")))]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Llista de tuples ordenada:", sorted_tuples)
