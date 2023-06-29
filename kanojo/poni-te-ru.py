n = int(input())


def f(n):
    while n > 0:
        yield n
        n -= 1
    yield "0!!"


for result in f(n):
    print(result)
