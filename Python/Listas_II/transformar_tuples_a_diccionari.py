tuples = [tuple(input("Introdueix un tuple (clau, valor) separat per coma: ").split(',')) for _ in range(int(input("Quants tuples? ")))]
dictionary = {key: value for key, value in tuples}
print("Diccionari:", dictionary)
