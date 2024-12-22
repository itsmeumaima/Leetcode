class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s)!=len(t)):
            return False
        s_dic={}
        t_dic={}
        for i in s:
            if i not in s_dic:
                s_dic[i]=1
            if i in s_dic:
                s_dic[i]+=1  
        for i in t:
            if i not in t_dic:
                t_dic[i]=1
            if i in t_dic:
                t_dic[i]+=1   
        return s_dic==t_dic
