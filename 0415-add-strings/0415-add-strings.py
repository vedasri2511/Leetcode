class Solution:
    def addStrings(self, num1, num2):
        i, j, carry = len(num1)-1, len(num2)-1, 0
        res = []

        while i >= 0 or j >= 0 or carry:
            x = ord(num1[i]) - 48 if i >= 0 else 0
            y = ord(num2[j]) - 48 if j >= 0 else 0

            s = x + y + carry
            res.append(chr(s % 10 + 48))
            carry = s // 10

            i -= 1
            j -= 1

        return ''.join(reversed(res))