def high_and_low(string):
    numbers = [int(n) for n in string.split()]
    return " ".join([str(max(numbers)), str(min(numbers))])

print(high_and_low("1 2 3 4 5"))
