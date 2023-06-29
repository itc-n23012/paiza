n = int(input())
s = input()


def f(n, s):
    return "\n".join([s] * n)


result = f(n, s)
print(result)
