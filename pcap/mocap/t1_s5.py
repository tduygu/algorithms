def sum_list(args, fun):
    z = 0
    for x in args:
        z = z+ fun(x)
    return z

print(sum_list(([ex//2 for ex in range(5)]), lambda x: 1 if x>1 else 0))
