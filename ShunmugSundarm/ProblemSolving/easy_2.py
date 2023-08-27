def steps_to_one(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        steps += 1
    return steps

print(steps_to_one(12))
