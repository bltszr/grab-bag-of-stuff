def gcd_iter(a, b):
    x = max(a, b)
    y = min(a, b)
    while y: # while x is not 0
        x, y = y, x % y
    return x