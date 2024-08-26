class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=set()
        for i in s:
            if i in new:
                return i
            else:
                new.add(i)    
