def gcd_rec(a, b):
    x = max(a, b)
    y = min(a, b)
    return gcd_rec(y, x % y) if y else x