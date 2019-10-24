def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
if __name__ == "__main__":
    a = int(input("Input the greater integer: "))
    b = int(input("Input the lesser integer: "))
    print("The greatest common divisor is %d" % gcd(a, b))