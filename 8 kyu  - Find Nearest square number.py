'''
Find Nearest square number

Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.
For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11,
 than 100, the square of 10.
If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.
'''

import math
def nearest_sq(n):
    m = n
    if math.isqrt(abs(n)) ** 2 == n:
        return n
    else:
        while math.isqrt(abs(n)) ** 2 != n or math.isqrt(abs(m)) ** 2 != m:
            n -= 1
            m += 1
            if math.isqrt(abs(n)) ** 2 == n:
                return n
            if math.isqrt(abs(m)) ** 2 == m:
                return m

print(nearest_sq(138))