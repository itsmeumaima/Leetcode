class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=1
            elif i in dic:
                dic[i]+=1
        new=[dic[i] for i in dic]
        for i in range(len(new)):
            for j in range(i+1,len(new)):
                if new[i]==new[j]:
                    return False
        return True                
