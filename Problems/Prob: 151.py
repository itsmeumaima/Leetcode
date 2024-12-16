class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=[]
        for i in s.split():
            lst.append(i)
        ans=""
        for i in range(len(lst),0,-1):
            ans+=lst[i-1]
            if i!=1:
                ans+=" "
        return ans
        
