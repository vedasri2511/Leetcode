class Solution:
    def canConstruct(self, ransomNote, magazine):
        cnt = [0]*26

        for c in magazine:
            cnt[ord(c)-97] += 1

        for c in ransomNote:
            i = ord(c)-97
            if cnt[i] == 0:
                return False
            cnt[i] -= 1

        return True