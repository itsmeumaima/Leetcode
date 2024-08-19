class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        var=0
        count=0
        for i in s:
            if s=="L":
                var+=1
            elif s=="R":
                var-=1
            elif var==0: 
                count+=1
        return count                
