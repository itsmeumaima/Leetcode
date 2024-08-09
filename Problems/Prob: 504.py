class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        ans = ""
        is_negative = num < 0
        num = abs(num)

        while num > 0:
            ans = str(num % 7) + ans
            num //= 7

        if is_negative:
            ans = "-" + ans
        
        return ans       
