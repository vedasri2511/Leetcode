class Solution:
    def repeatedSubstringPattern(self, s):
        lps = [0]*len(s)
        j = 0

        for i in range(1, len(s)):
            while j and s[i] != s[j]:
                j = lps[j-1]

            if s[i] == s[j]:
                j += 1
                lps[i] = j

        return lps[-1] > 0 and len(s) % (len(s)-lps[-1]) == 0