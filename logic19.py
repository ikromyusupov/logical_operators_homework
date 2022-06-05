def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x1 = a % 10
    a //= 10

    x2 = a % 10
    a //= 10

    x3 = a % 10
    a //= 10

    x4 = a % 10
    a //= 10

    return ((x1 == x3) and (x2 == x4)) or ((x3 == x1) and (x2 == x4))