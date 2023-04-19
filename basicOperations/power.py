def power(base, exp):
    assert int(exp) == exp, 'The exponent must be integer number only'
    print(f"base= {base} - exponent= {exp}")
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp+1)
    return base * power(base, exp-1)

#print(power(2, 4))
#print(power(-1,7))
#print(power(3.2, 2))
#print(power(2,1.2))
print(power(2, -1))

