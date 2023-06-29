def f():
    count = 0
    for i in range(5):
        d, e = input().split()
        count += 1 if d == e else 0
    return "OK" if count >= 3 else "NG"


result = f()
print(result)
