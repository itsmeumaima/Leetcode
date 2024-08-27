class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        new=""
        if n%2!=0:
            for i in range(n):
                new+="a"
        else:
            for i in range(n-1):
                new+="b"
            new+="a"
        return new                


        
