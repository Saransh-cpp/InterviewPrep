def divide(dividend, divisor):
    sign = -1 if (
        dividend < 0 and divisor >=0
        ) or (
        divisor < 0 and dividend >=0
        ) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    res = 0
    while (dividend >= divisor):
        count = 0
        while (divisor << count <= dividend):
            count += 1
        res += 1 << (count - 1)
        dividend -= divisor << (count - 1)
    return min(sign * res, 2 ** 31 - 1)
