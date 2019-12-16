def remove_url_anchor(url):
    """
    >>> remove_url_anchor("www.codewars.com#about")
    'www.codewars.com'
    >>> remove_url_anchor("www.codewars.com/katas/?page=1#about")
    'www.codewars.com/katas/?page=1'
    >>> remove_url_anchor("www.codewars.com/katas/")
    'www.codewars.com/katas/'
    """
    url = url.split("#")
    return url[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
