def reversed(number):
    return int(str(int(number))[::-1])

def formatter(number):
    return format(int(number), 'b'), format(int(number), 'o')