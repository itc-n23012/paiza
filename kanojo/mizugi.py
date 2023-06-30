n = int(input())


def f(n):
    import math

    a = math.factorial(n)
    b = str(a).rstrip("0")
    c = min(len(b), 9)
    return b[-c:].lstrip("0")


result = f(n)
print(result)


# 大きい桁の計算の仕方がわからなかったです
