def strength(password):
    control = [0, 0, 0]
    if len(password) > 7:
        control[0] = 1

    for l in password:
        if l == l.upper():
            control[1] = 1
            break

    for l in password:
        if l.isdigit():
            control[2] = 1
            break

    if all(control):
        return "Strong Password"
    else:
        return "Weak Password"