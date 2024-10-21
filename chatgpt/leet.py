def convert_to_base_7(num: int) -> str:
    if num == 0:
        return "0"
    
    negative = num < 0
    num = abs(num)
    
    base_7 = []
    
    while num > 0:
        base_7.append(str(num % 7))
        num //= 7
    
    result = ''.join(reversed(base_7))
    
    return '-' + result if negative else result

# Test cases
print(convert_to_base_7(100))  # Output: "202"
print(convert_to_base_7(-7))   # Output: "-10"
