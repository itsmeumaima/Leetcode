class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans=""
        for i in range(len(command)):
            if command[i]=='G' or command[i]=='a' or command[i]=='l':
                ans+=command[i]
            elif command[i:i+2]=='()':
                ans+='o'
        return ans            
