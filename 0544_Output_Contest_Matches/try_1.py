class Solution:
    def findContestMatch(self, n: int) -> str:
        '''
        一直依照 (先抓最大，配當前最小) 去組成string即可
        '''
        def getString(s1, s2):
            return "({},{})".format(s1, s2)
        
        
        
        # init
        string_list = []
        for i in range(n//2):
            string_list.append(getString(str(i+1), str(n-i)))
        
        # loop until string_list length = 1
        while len(string_list) > 1:
            length = len(string_list)
            for i in range(length//2):
                string_list[i] = getString(string_list[i], string_list[-1])
                string_list.pop()
        
        return string_list[0]
        