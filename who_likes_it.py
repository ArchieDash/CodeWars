def like(func):
    """
    >>> likes([])
    'no one likes this'
    >>> likes(["Peter"])
    'Peter likes this'
    >>> likes(["Jacob", "Alex"])
    'Jacob and Alex like this'
    >>> likes(["Max", "John", "Mark"])
    'Max, John and Mark like this'
    >>> likes(["Alex", "Jacob", "Mark", "Max"])
    'Alex, Jacob and 2 others like this'
    """
    def wrapper(*args):
        if len(*args) <  2:
            return func(*args) + " likes this"
        else:
            return func(*args) + " like this"
    return wrapper


@like
def likes(names: list) -> str:
    if names:
        if len(names) == 1:
            return names[0]
        elif len(names) == 2:
            return " and ".join(names) 
        elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]}"
        elif len(names) > 3:
            return f"{names[0]}, {names[1]} and {len(names)-2} others"
    else:
        return "no one"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
