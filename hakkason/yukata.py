def f(ts):
    sa = 0
    cost = 0

    for i in range(24):
        sa = max(sa - 1, 0)
        if str(i) in ts:
            if ts[str(i)] == "in":
                sa += 5
            else:
                sa += 3
        if sa == 0:
            cost += 1
        else:
            cost += 2
    return cost


n = int(input())
ts = dict(input().split() for _ in range(n))
result = f(ts)
print(result)
