class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        numbers = list(counter.keys())
        
        def quick_select(numbers, _k):
            if not numbers:
                return []
            
            pivot_index = random.randint(0, len(numbers)-1)
            numbers[pivot_index], numbers[-1] = numbers[-1], numbers[pivot_index]
            count_pivot = counter[numbers[-1]]
            
            i = j = 0
            while j < len(numbers):
                count_cur = counter[numbers[j]]
                
                if count_cur < count_pivot:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    i += 1
                j += 1
            
            numbers[i], numbers[-1] = numbers[-1], numbers[i]
            
            if i == _k:
                return numbers[i:]
            elif i > _k:
                return numbers[i:] + quick_select(numbers[:i], _k)
            else:
                return quick_select(numbers[i:], _k-i)
        
        return quick_select(numbers, len(numbers)-k)
