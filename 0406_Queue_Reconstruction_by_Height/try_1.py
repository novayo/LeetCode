class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 初始想法
        # h由大到小 且 k由小到大去排
        # list 利用insert去排序

        '''
        Original input list:          [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        Expect sorted list like that: [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        '''
        people.sort(key = lambda element: element[1])
        people.sort(key = lambda element: element[0], reverse = True)
        
        ans = []
        for element in people:
            tmpK, index = 0, 0
            for ans_element in ans:
                if ans_element[0] >= element[0]:
                    tmpK, index = tmpK+1, index+1
                else:
                    index += 1
                if tmpK > element[1]:
                    index -= 1
                    break
            ans.insert(index, element)
        return ans
