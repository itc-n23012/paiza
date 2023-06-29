s = int(input())
t = int(input())


def f(s, t):
    a = "-" * s
    return a[: t - 1] + "+" + a[t:]


result = f(s, t)
print(result)
