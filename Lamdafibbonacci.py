from functools import reduce

# Define a lambda function to generate the Fibonacci sequence
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Generate the Fibonacci series with 50 elements
fib_series = fibonacci(50)

# Print
print(fib_series)
