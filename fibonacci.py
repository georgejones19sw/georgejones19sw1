def generate_fibonacci(n):
    fibonacci_sequence = []
    if n >= 1:
        fibonacci_sequence.append(0)
    if n >= 2:
        fibonacci_sequence.append(1)
    for i in range(2, n):
        next_num = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence

# Prompt the user to enter the number of terms
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(num_terms)

# Display the sequence
print(f"The Fibonacci sequence with {num_terms} terms is:")
for num in fibonacci_sequence:
    print(num, end=" ")
