"""Return "min max" from string of numbers"""
def high_and_low(string: str) -> str:
    numbers = [int(n) for n in string.split()]
    return " ".join([str(max(numbers)), str(min(numbers))])
