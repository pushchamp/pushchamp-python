"""
    Pushchamp Exceptions
"""

class EmptyChannel(Exception):
    """raise for empty channel"""
    pass

class InvalidType(Exception):
    """raise if object is not of expected type"""
    def __init__(self, key, expected_type, actual_type):
        msg = "'%s' is not valid. Expected: %s, Got: %s" % (key, expected_type, actual_type)
        super(InvalidType, self).__init__(msg)
