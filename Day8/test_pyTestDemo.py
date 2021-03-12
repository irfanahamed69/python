from isupper import check_is_upper

def test_boolean_is_upper():
    assert check_is_upper('HELLO') == True

def test_boolean_is_notUpper():
    assert check_is_upper('hello') == True
