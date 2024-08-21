class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_value = 0
        
        for s in strs:
            if s.isdigit():
                value = int(s)  # Numeric representation if all digits
            else:
                value = len(s)  # Length of the string otherwise
            
            if value > max_value:
                max_value = value
        
        return max_value
