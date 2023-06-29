n = int(input())


def f(n):
    for i in range(n):
        m = int(input())
        a = 6 * 60
        b = m // 3

        c = (7 * 60 - (a + b)) % (24 * 60)
        yield (f"{c // 60:02}:{c % 60:02}")


for result in f(n):
    print(result)
