# Constants
MOD = 10**9 + 7
MAX_LENGTH = 100  # Assumed maximum length of any word in the input string

# Helper function to precompute factorials and modular inverses up to MAX_LENGTH
def precompute_factorials(max_len, mod):
    fact = [1] * (max_len + 1)
    inv_fact = [1] * (max_len + 1)
    
    # Compute all factorials % mod
    for i in range(2, max_len + 1):
        fact[i] = fact[i-1] * i % mod
    
    # Compute inverses using Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p)
    inv_fact[max_len] = pow(fact[max_len], mod - 2, mod)
    
    # Compute inverse factorials using the relation inv_fact[n-1] = inv_fact[n] * n
    for i in range(max_len - 1, 0, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % mod
    
    return fact, inv_fact

# Function to calculate the number of distinct anagrams of a word
def count_anagrams(word, fact, inv_fact, mod):
    from collections import Counter
    freq = Counter(word)
    word_length = len(word)
    
    # Total anagrams is word_length! / (freq[ch1]! * freq[ch2]! * ...)
    total_anagrams = fact[word_length]
    for f in freq.values():
        total_anagrams = total_anagrams * inv_fact[f] % mod
    
    return total_anagrams

# Function to compute the number of distinct anagrams of the whole string s
def num_distinct_anagrams(s, mod):
    words = s.split()  # Split into words
    fact, inv_fact = precompute_factorials(MAX_LENGTH, mod)
    
    result = 1
    for word in words:
        result = result * count_anagrams(word, fact, inv_fact, mod) % mod
    
    return result

# Test the function with the example cases
test_case_1 = "too hot"
test_case_2 = "aa"

output_1 = num_distinct_anagrams(test_case_1, MOD)
output_2 = num_distinct_anagrams(test_case_2, MOD)

output_1, output_2
