from collections import Counter
from math import factorial

def count_anagrams(s: str) -> int:
    MOD = 10**9 + 7

    def word_anagrams(word):
        count = Counter(word)
        result = factorial(len(word))
        for freq in count.values():
            result //= factorial(freq)
        return result

    words = s.split()
    result = 1
    for word in words:
        result = (result * word_anagrams(word)) % MOD

    return result

# Example usage:
s1 = "too hot"
s2 = "aa"
print(count_anagrams(s1))  # Output: 18
print(count_anagrams(s2))  # Output: 1
