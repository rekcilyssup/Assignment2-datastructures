"""
Fibonacci sequence calculation.
"""

def fibonacci(nth_fib):
    """
    Return the nth Fibonacci number.
    """
    first, second = 0, 1
    for _ in range(nth_fib):
        first, second = second, first + second
    return first


if __name__ == "__main__":
    fibonacci(10)
