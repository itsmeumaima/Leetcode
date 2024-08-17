class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lower = 'abcdefghijklmnopqrstuvwxyz'
        dic = {lower[i]: alpha[i] for i in range(26)}
        
        unique_transformations = {"".join(dic[char] for char in word) for word in words}
        
        return len(unique_transformations)
