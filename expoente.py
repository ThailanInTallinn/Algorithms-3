def power(x, y):
    if y == -1:
        return (1 / x)
    if y == 0:
        return 1
    if y == 1:
        return x
    if x == 0:
        return 0

    if y < 0:
        return power(x, y + 1) * (1 / x)
    return power(x, y - 1) * x


result = power(2, -4)
print(result)
