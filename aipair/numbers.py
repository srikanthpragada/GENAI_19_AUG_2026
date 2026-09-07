def isprime(num: int) -> bool:
    """Determine whether ``num`` is a prime number.

    A prime number is an integer greater than one that has no positive
    divisors other than one and itself. The function tests possible divisors
    only through the square root of ``num``, because any larger factor would
    be paired with a smaller factor that had already been tested.

    Args:
        num: The integer to evaluate.

    Returns:
        ``True`` when ``num`` is prime; otherwise, ``False``. Values less
        than or equal to one are not prime.

    Examples:
        >>> isprime(7)
        True
        >>> isprime(12)
        False
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isperfect(num: int) -> bool:
    """Determine whether ``num`` is a perfect number.

    A perfect number is a positive integer equal to the sum of its positive
    proper divisors, excluding the number itself. This function finds those
    divisors, adds them together, and compares the sum with ``num``.

    Args:
        num: The positive integer to evaluate.

    Returns:
        ``True`` when the sum of ``num``'s positive proper divisors equals
        ``num``; otherwise, ``False``. Non-positive values are not perfect
        numbers.

    Examples:
        >>> isperfect(6)
        True
        >>> isperfect(10)
        False
    """
    if num <= 0:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
