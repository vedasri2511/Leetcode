class Solution:
    def detectCapitalUse(self, word):
        c = sum('A' <= ch <= 'Z' for ch in word)
        return c == len(word) or c == 0 or (c == 1 and 'A' <= word[0] <= 'Z')