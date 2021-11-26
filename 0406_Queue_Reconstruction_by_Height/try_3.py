class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[1], x[0]))
        
        for i in range(len(people)):
            
            # 記錄總共有幾個大於target
            bigger_num = 0
            for j in range(i-1, -1, -1):
                if people[j][0] >= people[i][0]:
                    bigger_num += 1
            
            # 調整到第一個符合的即可
            j = i
            while j > 0 and people[j][1] < bigger_num:
                if people[j-1][0] >= people[j][0]:
                    bigger_num -= 1
                people[j-1], people[j] = people[j], people[j-1]
                j -= 1
        
        return people
