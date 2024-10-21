#META AI
class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        words = s.split()
        res = 1
        max_len = max(len(word) for word in words)
        factorial = [1]
        
        for i in range(1, max_len+1): 
            factorial.append((factorial[-1] * i) % MOD)
        
        inverse_factorial = [pow(factorial[-1], MOD-2, MOD)]
        for i in range(max_len, 0, -1):
            inverse_factorial.append((inverse_factorial[-1] * i) % MOD)
        inverse_factorial.reverse()
        
        for word in words:
            char_count = {}
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
            
            word_anagrams = 1
            for count in char_count.values():
                word_anagrams *= factorial[count]
                word_anagrams %= MOD
            
            word_permutations = factorial[len(word)]
            for count in char_count.values():
                word_permutations *= inverse_factorial[count]
                word_permutations %= MOD
            
            res *= word_permutations
            res %= MOD
        
        return res