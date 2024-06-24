import math
def palindrome(number):
    return int(number != 0) and ((number % 10) * \
            (10**int(math.log(number, 10))) + \
                        palindrome(number // 10))
n = int(input())
palindrome()