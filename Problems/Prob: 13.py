class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        prev_value = 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for char in s:
            current_value = dict[char]
            if current_value > prev_value:
                num += (current_value-2*prev_value)
            else:
                num += current_value
            prev_value = current_value
    
        return num
        

