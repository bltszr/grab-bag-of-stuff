 def reverse(self, x: int) -> int:
        result = 0
        if (x < -2 ** 31) or (x > (2 ** 31) -1):
            return 0
        else:
            y = abs(x)
            while y != 0:
                last_num = y % 10
                result = (result * 10) + last_num
                y //= 10
            if x < 0:
                if result > (2 ** 31):
                    return 0
                else:
                    return result * - 1
            else:
                if result > ((2 ** 31) - 1): # integer overflow checking
                    return 0                 # this isn't actually necessary,               
                else:                        # it's specific for the leetcode
                    return result            # problem