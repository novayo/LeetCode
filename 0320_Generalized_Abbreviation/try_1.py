class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        '''
        word
        1 => 1ord .. 1o1d ...
        2 => 2rd ...
        3 =>
        4 => 
        
        is_valid => False => 移除我的loop的set
            => 數字字母間格 => 頭尾, 2數字之間, 長度<3
        '''
        
        bitmask = set()
        def dfs(cur_string, index):
            
            bitmask.add(cur_string) 
            
            if index >= len(cur_string):
                return

            dfs(cur_string, index+1)
            dfs(cur_string[:index] + '1' + cur_string[index+1:], index+1)
        
        dfs('0'*len(word), 0)
        
        ans = []
        for string in bitmask:
            tmp = ''
            count = 0
            for i in range(len(string)):
                if string[i] == '1':
                    count += 1
                else:
                    if count > 0:
                        tmp += str(count)
                    count = 0
                    tmp += word[i]
            if count > 0:
                tmp += str(count)
            ans.append(tmp)
        return ans
        
        