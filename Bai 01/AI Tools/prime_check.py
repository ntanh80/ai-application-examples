def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập n: "))

primes = []
for x in range(2, n + 1):
    if is_prime(x):
        primes.append(x)

print("Các số nguyên tố <=", n, "là:", primes)
