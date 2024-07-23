import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    n, d = denom2 * numer1 + denom1 * numer2, denom1 * denom2
    if math.gcd(n, d) != 1:
        n, d = n // math.gcd(n, d), d // math.gcd(n, d)
    return [n, d]