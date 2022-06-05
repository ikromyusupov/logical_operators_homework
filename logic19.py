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

    return (x1 + x2) == (x3 + x4) and (x3 + x2) == (x1 + x4)