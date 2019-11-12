import string


def alphabet_position(text):
    alphabet = [str(letter) for letter in string.ascii_lowercase]
    indexes = [alphabet.index(letter)+1 for letter in text.lower() if letter in alphabet]
    return ' '.join([str(i) for i in indexes])
