class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index_sum = float('inf')
        table_ans = collections.defaultdict(list)
        table_list1 = {}
        
        for i in range(len(list1)):
            table_list1[list1[i]] = i
        
        for i, l in enumerate(list2):
            if l in table_list1:
                sum = table_list1[l] + i
                if sum <= min_index_sum:
                    min_index_sum = sum
                    table_ans[min_index_sum].append(l)
        
        return table_ans[min_index_sum]