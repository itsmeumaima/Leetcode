class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=[i for i in s if i in "aeiouAEIOU"]
        new=""
        count=0
        for i in s:
            if i in "aeiouAEIOU":
                count+=1
                new+=lst[-count]
            else:
                new+=i
        return new          


        
