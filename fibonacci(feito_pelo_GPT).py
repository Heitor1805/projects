def fibonacci_sequence(n):
    fib = [0, 1]  # Initial values for the Fibonacci sequence
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])  # Add the last two numbers
    return fib[:n]  # Return the sequence up to `n` elements

# Get user input
num = int(input("Type the number of Fibonacci terms: "))

# Call the function and print the result
if num <= 0:
    print("Please type a positive integer.")
else:
    print(f"Fibonacci sequence: {fibonacci_sequence(num)}")
