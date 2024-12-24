num_terms = int(input("Enter the number of terms: "))
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
fib_sequence = fibonacci(num_terms)
print(f"The Fibonacci sequence with {num_terms} terms is:")
print(fib_sequence)
