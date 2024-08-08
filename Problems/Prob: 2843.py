class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for i in range(low, high + 1):
            num_str = str(i)
            # Check if the length of the string is even
            if len(num_str) % 2 == 0:
                mid = len(num_str) // 2
                # Calculate the sum of the first half and the second half
                sum_first_half = sum(int(digit) for digit in num_str[:mid])
                sum_second_half = sum(int(digit) for digit in num_str[mid:])
                # Compare the sums
                if sum_first_half == sum_second_half:
                    count += 1
        return count

