"""
code provided by Nikita Tiwari of GeeksforGeeks.
This is an iterative algorithm to find the result of
some integer x raised to the power of y in mod p.
This is done by the rule of (ab mod n) being equal
to (((a mod n)(b mod n)) mod n).
"""

def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 