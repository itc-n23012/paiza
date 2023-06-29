n = int(input())
m1 = int(input())
x = list(map(int, input().split()))
m2 = int(input())
y = list(map(int, input().split()))


def f(x, y):
    a = []
    for i in y:
        if i not in x:
            a.append(i)
    return sorted(a) if len(a) != 0 else None


result = f(x, y)
print(*result, sep=" ") if f(x, y) != None else print(result)
