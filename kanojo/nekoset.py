s = input()


def f(s):
    list = [0] * 4
    c = s.count("c")
    a = s.count("a")
    t = s.count("t")
    cat = [c, a, t]
    list[0] = min(cat)
    list[1] = max(cat) - c
    list[2] = max(cat) - a
    list[3] = max(cat) - t
    return list


result = f(s)
print("\n".join(map(str, result)))
