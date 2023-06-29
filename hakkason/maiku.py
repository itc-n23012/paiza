n = int(input())
m = int(input())


def f(n, m):
    return m // (n * 2) + 1 if m % (n * 2) != 0 else m // (n * 2)


result = f(n, m)
print(result)
