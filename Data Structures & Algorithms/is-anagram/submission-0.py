class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 = dict()
        dict2 = dict()
        for char1,char2 in zip(s,t):
            if char1 in dict1:
                dict1[char1] +=1
            else:
                dict1[char1] = 1
            if char2 in dict2:
                dict2[char2] +=1
            else:
                dict2[char2] = 1

        if dict1 == dict2:
            return True
        else:
            return False
