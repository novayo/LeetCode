class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''
        pass n sec 
            => start a -> start b => b-a
            => start a -> end b => b-a+1
            => end a -> start b => b-a-1
            => end a -> end b   => b-a
        '''
        def getInfo(string):
            tmp = string.split(':')
            return {
                'id': int(tmp[0]),
                'tag': tmp[1],
                'time': int(tmp[2])
            }
        
        def addAns(id, delta):
            nonlocal ans
            if id >= len(ans):
                ans.extend([0] * (id-len(ans)+1))
            ans[id] += delta
        
        ans = []
        stack = []
        cur_time = 0
        preInfo = None
        
        # init
        info = getInfo(logs[0])
        preInfo = info
        cur_time = info['time']
        stack.append(info)
        
        # loop
        for log in logs[1:]:
            info = getInfo(log)
            
            if preInfo['tag'] == 'start' and info['tag'] == 'start':
                addAns(preInfo['id'], info['time'] - cur_time)
                stack.append(info)
            elif preInfo['tag'] == 'start' and info['tag'] == 'end':
                addAns(info['id'], info['time'] - cur_time + 1)
                stack.pop()
            elif preInfo['tag'] == 'end' and info['tag'] == 'start':
                if stack:
                    addAns(stack[-1]['id'], info['time'] - cur_time - 1)
                stack.append(info)
            else:
                addAns(info['id'], info['time'] - cur_time)
                stack.pop()
            
            cur_time = info['time']
            preInfo = info
        
        return ans
            
