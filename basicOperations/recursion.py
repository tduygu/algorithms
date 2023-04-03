class Recursion:
    def factorial(self, n):
        assert 0 <= n == int(n), 'The number must be positive integer only!'
        if n in [0, 1]:
            return 1
        else:
            return n * self.factorial(n-1)

    def fibonacci(self, n):
        assert n >= 0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer'
        if n in [0, 1]:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


r = Recursion()
print(r.factorial(3))
print(r.fibonacci(7))
