class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        '''
        依照end排序過後，將跑過的課都選起來，只要總時間沒有超過當前end就算合理
        
        只要超過end，就將最大的start刪除直到合理，這部分可以用max heap
        
        因為每一次都將最長的start去除，因此就能保證可以greedy的取到最長
        而且，排序end就能將時間也考慮進去，也就是先選最早消失的
        '''
        courses.sort(key=lambda x: x[1])
        
        heap = []
        time = 0
        for start, end in courses:
            time += start
            heapq.heappush(heap, -start) # max heap
            while time > end:
                time += heapq.heappop(heap)
        
        return len(heap)
