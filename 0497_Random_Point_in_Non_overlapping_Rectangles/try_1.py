class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rect_list = []
        self.accept_probility = []
        
        area = []
        for x1, y1, x2, y2 in rects:
            self.rect_list.append((x1, x2, y1, y2))
            area.append((x2-x1+1)*(y2-y1+1))
        
        s = sum(area)
        for i in range(len(area)):
            self.accept_probility.append(area[i] / s)

    def pick(self) -> List[int]:
        index = random.randint(0, len(self.rect_list)-1)
        while random.random() >= self.accept_probility[index]:
            index = random.randint(0, len(self.rect_list)-1)
        
        rect = self.rect_list[index]
        x = random.randint(rect[0], rect[1])
        y = random.randint(rect[2], rect[3])
        
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()