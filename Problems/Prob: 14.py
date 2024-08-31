class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Find the minimum length string in the list to limit the prefix search
        min_length = min(len(s) for s in strs)
        
        # Initialize the prefix to an empty string
        prefix = ""
        
        # Compare characters one by one up to the length of the shortest string
        for i in range(min_length):
            # Get the current character from the first string
            current_char = strs[0][i]
            
            # Check this character against all other strings
            for s in strs:
                if s[i] != current_char:
                    return prefix
            prefix += current_char
        
        return prefix
