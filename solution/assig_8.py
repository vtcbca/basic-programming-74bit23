def print_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(chr(65 + j), end=' ')
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end=' ')
        print()
n = int(input("Enter the value of n: "))
print_pattern(n)
