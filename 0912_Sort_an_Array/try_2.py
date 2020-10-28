class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        button-up merge sort
        '''
        queue = collections.deque()
        
        for num in nums:
            queue.append([num])
            
        while len(queue) > 1:
            
            a = queue.popleft()
            b = queue.popleft()
            
            ret = []
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ret.append(b[j])
                    j += 1
            ret.extend(a[i:])
            ret.extend(b[j:])
            
            queue.append(ret)
        
        return queue.pop()