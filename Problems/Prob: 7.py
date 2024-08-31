class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        new_str = str(x)
        reversed_str = new_str[::-1]
        reversed_num = int(reversed_str)
        
        # Check for overflow
        if reversed_num > 2**31 - 1:
            return 0
        
        return sign * reversed_num
