# Function to calculate Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci(n)

# Output the sequence
print(f"Fibonacci sequence of {n} terms: {fib_sequence}")
