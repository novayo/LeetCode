class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        O(len(updates) + length) / O(len(updates) + length)
        O(10**5) / O(10**5)

        1. 找出相同的i~j 並把 offset 加起來

        [1,3,3], [1,3,2], [1,4,2]
        1~3 => 7
        4 => 2

        1 => 7   => curNum + 7  => nums[1] = 7 curNum
                                => nums[2] = 7 curNum
                                => nums[3] = 7 curNum
        4 => -5 => curNum - 5   => nums[4] = 2 curNum
        5 => -2 => curNum - 2   => nums[5] = 0 curNum...
        '''
        offsetDict = collections.Counter()
        for i, j, offset in updates:
            offsetDict[i] += offset
            offsetDict[j+1] -= offset

        arr = [0] * length
        curNum = 0
        for i in range(length):
            if i in offsetDict:
                curNum += offsetDict[i]
            arr[i] = curNum
        return arr