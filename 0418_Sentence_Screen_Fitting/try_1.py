class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        '''
        一般的想法：O(ans * n)
        
        O(n)
        紀錄 第一個字，從i開始，end在哪
        紀錄0開始，會佔幾列 => 
            餘數最後再跑一次即可
            
        '''
        ans = 0
        found = set()
        
        flag = True
        batch_col = -float('inf')
        batch_row = -float('inf')
        batch_ans = -float('inf')
        
        index_s = 0
        cur_row = 0
        
        buffer = -1
        while cur_row < rows:
            target = sentence[index_s]
            
            if buffer + 1 + len(target) <= cols:
                buffer += 1 + len(target)
                index_s += 1
            else:
                cur_row += 1
                buffer = -1
            
            if index_s >= len(sentence):
                index_s = 0
                ans += 1
                
                if flag and buffer in found:
                    batch_col = buffer
                    batch_row = cur_row
                    batch_ans = ans
                    flag = False
                    continue
                
                if not flag and buffer == batch_col:
                    batch_row = cur_row - batch_row
                    batch_ans = ans - batch_ans
                    
                    e = (rows - cur_row) // batch_row
                    cur_row += batch_row * e
                    ans += batch_ans * e
                    if cur_row >= rows:
                        ans -= 1
                        break
                
                found.add(buffer)
        
        return ans
