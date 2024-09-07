class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """      
        dic={} 
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1    
        for index, char in enumerate(s):
            if dic[char] == 1:
                return index
        
        return -1   
