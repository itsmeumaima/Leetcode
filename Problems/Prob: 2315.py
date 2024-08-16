class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        within_bars = False
        
        for char in s:
            if char == '|':
                within_bars = not within_bars 
            elif char == '*' and not within_bars:
                count += 1
        
        return count
