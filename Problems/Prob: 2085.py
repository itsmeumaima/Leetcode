class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        new1={}
        new2={}
        for i in words1:
            if i in new1:
                new1[i]+=1
            else:
                new1[i]=1
        for i in words2:
            if i in new2:
                new2[i]+=1
            else:
                new2[i]=1
        count = 0
        for word in new1:
            if new1[word] == 1 and new2.get(word, 0) == 1:
                count += 1
        
        return count       


