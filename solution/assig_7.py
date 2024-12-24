rows = 3

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("1", end=" ")
    print()