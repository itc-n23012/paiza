n, m = map(int, input().split())
s = input()
t = input()


def f(n, m, s, t):
    for i in s:
        if i in t:
            t = t.replace(i, "", 1)
    return len(t)


result = f(n, m, s, t)
print(result)
