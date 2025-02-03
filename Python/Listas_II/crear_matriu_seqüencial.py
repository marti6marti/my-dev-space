rows = int(input("Introdueix el nombre de files: "))
cols = int(input("Introdueix el nombre de columnes: "))
matrix = [[cols * i + j + 1 for j in range(cols)] for i in range(rows)]
print("Matriu:")
for row in matrix:
    print(row)
