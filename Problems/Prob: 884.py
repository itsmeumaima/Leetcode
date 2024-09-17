class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split()
        words2 = s2.split()
        freq = {}
        for word in words1:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        for word in words2:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        ans = [word for word in freq if freq[word] == 1]
        
        return ans    

        
