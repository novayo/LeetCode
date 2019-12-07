class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec1 as a model, if rec2 each point inside a model, then it must overlap

        if  (rec1[0] < rec2[0] < rec1[2] and rec1[1] < rec2[3] < rec1[3]) or\
            (rec1[0] < rec2[2] < rec1[2] and rec1[1] < rec2[3] < rec1[3]) or\
            (rec1[0] < rec2[0] < rec1[2] and rec1[1] < rec2[1] < rec1[3]) or\
            (rec1[0] < rec2[2] < rec1[2] and rec1[1] < rec2[1] < rec1[3]) or\
            ((rec1[0] <= rec2[0] <= rec1[2] and rec1[0] <= rec2[2] <= rec1[2]) and\
            (rec1[1] >= rec2[1] and rec2[3] >= rec1[3])) or\
            ((rec1[1] <= rec2[1] <= rec1[3] and rec1[1] <= rec2[3] <= rec1[3]) and\
            (rec1[0] >= rec2[0] and rec2[2] >= rec1[2])):
            return True
        rec1, rec2 = rec2, rec1
        if  (rec1[0] < rec2[0] < rec1[2] and rec1[1] < rec2[3] < rec1[3]) or\
            (rec1[0] < rec2[2] < rec1[2] and rec1[1] < rec2[3] < rec1[3]) or\
            (rec1[0] < rec2[0] < rec1[2] and rec1[1] < rec2[1] < rec1[3]) or\
            (rec1[0] < rec2[2] < rec1[2] and rec1[1] < rec2[1] < rec1[3]) or\
            ((rec1[0] <= rec2[0] <= rec1[2] and rec1[0] <= rec2[2] <= rec1[2]) and\
            (rec1[1] >= rec2[1] and rec2[3] >= rec1[3])) or\
            ((rec1[1] <= rec2[1] <= rec1[3] and rec1[1] <= rec2[3] <= rec1[3]) and\
            (rec1[0] >= rec2[0] and rec2[2] >= rec1[2])):
            return True
        return False
