def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for i, num in enumerate(fibonacci(10)):
    print(f"Fibonacci {i+1}: {num}")
```

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = fibonacci(10)
for i, num in enumerate(fib):
    print(f"Fibonacci {i+1}: {num}")
