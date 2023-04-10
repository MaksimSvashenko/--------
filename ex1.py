def f(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x > 2:
        return 2 * f(x - 1) + (x - 2) * f(x - 2)
print(f(6))