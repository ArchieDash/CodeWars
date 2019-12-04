from string import ascii_letters


def dec(func):
    def wrapper(*args):
        return " ".join(func(*args))
    return wrapper


@dec
def pig_it(_text):
    for word in _text.split(" "):
        if word[0] in ascii_letters:
            yield word[1:]+word[0]+"ay"
        else:
            yield word
