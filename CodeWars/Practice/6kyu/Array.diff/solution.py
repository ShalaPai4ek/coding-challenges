a = [1, 2, 3, -3, 4]
b = [2, -3]

def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a

array_diff(a, b)
