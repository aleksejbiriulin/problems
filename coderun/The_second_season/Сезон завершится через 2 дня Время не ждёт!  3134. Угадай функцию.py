def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_phi(n):
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result / i
    if n > 1:
        result -= result / n
    return int(result)

n = int(input())
print(euler_phi(n))