#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    sum_add = add(a, b)
    sum_sub = sub(a, b)
    sum_mul = mul(a, b)
    sum_div = div(a, b)

    print("{} + {} = {}".format(a, b, sum_add))
    print("{} - {} = {}".format(a, b, sum_sub))
    print("{} * {} = {}".format(a, b, sum_mul))
    print("{} / {} = {}".format(a, b, sum_div))
