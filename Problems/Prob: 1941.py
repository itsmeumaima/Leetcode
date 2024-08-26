class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic=dict()
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        lst=[i for i in dic.values()]
        ans=list(set(lst))
        if len(ans)==1:
            return True
        else:
            return False    

        
