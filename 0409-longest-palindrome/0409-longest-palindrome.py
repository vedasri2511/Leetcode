class Solution:
    def longestPalindrome(self, s):
        m = 0
        for c in s: m ^= 1 << (ord(c)-65)
        return len(s) - bin(m).count('1') + (m != 0)