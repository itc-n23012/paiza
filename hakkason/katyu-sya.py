n, p = map(int, input().split())
m, q = map(int, input().split())


def f(n, p, m, q):
    a = n * p
    b = q * (n // m)
    if n % m != 0:
        b += q

    return a + b


result = f(n, p, m, q)
print(result)
