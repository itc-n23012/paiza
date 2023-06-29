n = int(input())


def f(n):
    return "lucky" if n % 7 == 0 else "unlucky"


result = f(n)
print(result)
