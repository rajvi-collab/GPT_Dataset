def convertToBase7(num: int) -> str:
    """
    Converts an integer to its base 7 representation.

    Args:
    num (int): The integer to be converted.

    Returns:
    str: The base 7 representation of the integer.
    """
    if num == 0:
        return "0"

    negative = False
    if num < 0:
        negative = True
        num = -num

    base7 = []
    while num > 0:
        base7.append(str(num % 7))
        num //= 7

    result = "".join(reversed(base7))
    return "-" + result if negative else result

print(convertToBase7(100))  # Expected output: "202"
print(convertToBase7(-7))   # Expected output: "-10"