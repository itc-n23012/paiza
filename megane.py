n = int(input())
a = list(map(int, input().split()))


def f(a, n):
    return sorted(a)[(n + 1) // 2 - 1]


result = f(a, n)
print(result)
