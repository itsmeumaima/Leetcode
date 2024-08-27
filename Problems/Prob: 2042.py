class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst=[int(i) for i in s.split() if i.isdigit()]
        for i in range(len(lst)-1):
            if lst[i]<lst[i+1]:
                pass
            else:
                return False    
        return True        
        
