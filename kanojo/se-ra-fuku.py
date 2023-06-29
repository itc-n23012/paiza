n = int(input())


def f(n):
    a = []
    for i in range(n):
        s = input()
        a.append(s)

    return "_".join(a)


result = f(n)
print(result)
