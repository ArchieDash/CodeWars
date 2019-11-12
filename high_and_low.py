def high_and_low(string):
    numbers = [int(n) for n in string.split()]
    return " ".join([str(max(numbers)), str(min(numbers))])
