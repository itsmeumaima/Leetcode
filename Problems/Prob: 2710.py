class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        while int(num[-1])==0:
            num=str(int(num)/10)
        return num    
