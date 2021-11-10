class Solution:
    def nextClosestTime(self, time: str) -> str:
        '''
        直接+1分鐘，找到第一個符合的即可
        '''
        hour, minute = time.split(':')
        kinds = set([hour[0], hour[1], minute[0], minute[1]])
        
        hour = int(hour)
        minute = int(minute)
        while True:
            minute += 1
            if minute >= 60:
                minute = 0
                hour += 1
                
                if hour >= 24:
                    hour = 0
            
            tmp = str(hour).zfill(2) + str(minute).zfill(2)
            flag = True
            for i in range(4):
                if tmp[i] not in kinds:
                    flag = False
                    break
            
            if flag:
                return tmp[:2] + ':' + tmp[2:]
            
