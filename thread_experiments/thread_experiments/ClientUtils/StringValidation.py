import re

def emptyString(string: str) -> bool:
    """
    This method checks if a string is empty\n
    Based on content
    """
    return not string or bool(re.fullmatch(r'[\s]*', string=string))
