

def check_is_upper(input):
    """
    The module to check if input is in upper case or not
    >>> 'HELLO' == 'Hello'
    False

    >>> 'HELLO' == 'HELLO'
    True
    """

    if (input.upper() == input):
        return True
    else: 
        return False

"""print(check_is_upper('ABC'))

if __name__ == "__main__":
    import doctest
    doctest.testmod()"""

# -v to check the doctest output