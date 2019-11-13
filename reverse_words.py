def reverse_words(text):
    text = [word[::-1] for word in text.split(" ")]
    return(" ".join(text))
