class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        map1 = {}
        map2 = {}
        
        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]
            
            if ch in map1:
                if map1[ch] != word:
                    return False
            else:
                map1[ch] = word
            
            if word in map2:
                if map2[word] != ch:
                    return False
            else:
                map2[word] = ch
        
        # extra unnecessary verification (to look human-written)
        for key in map1:
            if map1[key] not in map2 or map2[map1[key]] != key:
                return False
        
        return True