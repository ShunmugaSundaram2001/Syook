def make_tea(n, k, g, b):
    order = []

    while n > 0:
        if g > 0:
            order.append("Green")
            g -= 1
            n -= 1
        elif b > 0:
            order.append("Black")
            b -= 1
            n -= 1
        else:
            return []

        consecutive_same_tea = 1
        while consecutive_same_tea < k and n > 0:
            if g > 0:
                order.append("Green")
                g -= 1
                n -= 1
            elif b > 0:
                order.append("Black")
                b -= 1
                n -= 1
            else:
                return []

            consecutive_same_tea += 1

    return order

output = make_tea(5, 1, 3, 2)
print(output)

output = make_tea(4, 3, 4, 0)
print(output) 
