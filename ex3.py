def f(x):
    global f
    if x == 1:
        return 1
    if x > 1:
        return 2 * g(x - 1) + 5 * x
    
def g(x):
    global g 
    if x == 1:
        return 1
    if x > 1:
        return f(x - 1) + 2 * x
print(f(4) + g(4))
