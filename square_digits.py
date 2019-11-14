def square_digits(num):
    number = str(num)
    number = [int(n)**2 for n in number]
    number = ''.join([str(n) for n in number])
    return int(number)
