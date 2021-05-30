class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # 取得1總數
        total_1 = 0
        
        for value in arr:
            if value == 1:
                total_1 += 1
        
        # 若全為0
        if total_1 == 0:
            return [0, len(arr)-1]
        # 不能等分為3
        elif total_1 % 3 != 0:
            return [-1, -1]
        
        # 分成3等份 => 取得起始index
        parts_of_1 = total_1 // 3
        part_1 = [-1, 1]               # [起始index, 需要幾個1]
        part_2 = [-1, 1+parts_of_1]
        part_3 = [-1, 1+2*parts_of_1]
        
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                
                # 第一份：第一個1
                if count == part_1[1]:
                    part_1[0] = i
                
                if count == part_2[1]:
                    part_2[0] = i
                
                if count == part_3[1]:
                    part_3[0] = i
        
        # 從左到右看排序即可
        while part_3[0] < len(arr) and arr[part_1[0]] == arr[part_2[0]] == arr[part_3[0]]:
            part_1[0] += 1
            part_2[0] += 1
            part_3[0] += 1
        
        # 若有找到底，則回傳答案
        if part_3[0] == len(arr):
            return [part_1[0]-1, part_2[0]]
        else:
            return [-1, -1]
