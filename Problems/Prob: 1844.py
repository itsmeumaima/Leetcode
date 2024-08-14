class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=""
        import string
        alphabet=list(string.ascii_lowercase)
        for i in range(len(s)):
            if s[i].isdigit():
                ind=alphabet.index(s[i-1])
                temp=ind+int(s[i])
                new+=alphabet[temp]
            else:
                new+=s[i]
        return new            
