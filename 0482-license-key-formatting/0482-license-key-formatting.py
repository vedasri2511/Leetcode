class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()[::-1]
        res = []

        for i in range(0, len(s), k):
            res.append(s[i:i+k])

        return '-'.join(res)[::-1]