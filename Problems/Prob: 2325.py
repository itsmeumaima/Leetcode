class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        lst = [i for i in key if i != " "]
        new = []
        for char in lst:
            if char not in new:
                new.append(char)
                
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dic = {}
        for i in range(len(new)):
            dic[new[i]] = alphabet[i]
        
        ans = ""
        for char in message:
            if char == " ":
                ans += " "
            else:
                ans += dic[char]
        
        return ans
