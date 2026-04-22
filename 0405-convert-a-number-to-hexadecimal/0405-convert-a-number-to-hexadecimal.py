class Solution:
    def toHex(self, num):
        if not num: return "0"
        num &= 0xffffffff
        h = "0123456789abcdef"
        s = ""
        while num:
            s = h[num & 15] + s
            num >>= 4
        return s