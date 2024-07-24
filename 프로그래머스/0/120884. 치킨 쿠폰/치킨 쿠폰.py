def solution(chicken):
    coupon = chicken
    result = 0
    while coupon >= 10:
        result += coupon // 10
        coupon = coupon % 10 + (coupon // 10)
    return result