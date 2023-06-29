n = int(input())
m = int(input())


def f(n, m):
    return "".join(["R" if (i // n) % 2 == 0 else "W" for i in range(m)])


result = f(n, m)
print(result)
