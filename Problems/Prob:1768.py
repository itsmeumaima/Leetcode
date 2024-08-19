class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new = ""
        len1 = len(word1)
        len2 = len(word2)
        min_len = min(len1, len2)        
        for i in range(min_len):
            new += word1[i]
            new += word2[i]
        if len1 > len2:
            new += word1[min_len:]
        elif len2 > len1:
            new += word2[min_len:]
        
        return new
