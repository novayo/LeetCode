class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''
        start -> start => t2-t1
        start -> end => t2-t1+1
        end -> start => t2-t1-1
        end -> end => t2-t1
        
        start => append into stack
        end => pop from stack
        t1
        preactivity
        '''
        def parse_log(log):
            taskid, activity, time = log.split(':')
            return int(taskid), activity, int(time)
        
        
        ans = []
        stack = []
        t1 = -1
        preactivity = ''
        for log in logs:
            taskid, activity, t2 = parse_log(log)
            
            # increase answer
            while taskid >= len(ans):
                ans.append(0)
            
            # if first time
            if not preactivity:
                stack.append(taskid)
            elif preactivity == activity:
                ans[stack[-1]] += t2 - t1
            elif preactivity == 'start' and activity == 'end':
                ans[stack[-1]] += t2 - t1 + 1
            else:
                ans[stack[-1]] += t2 - t1 - 1
                
            if activity == 'end':
                stack.pop()
            else:
                stack.append(taskid)
            t1 = t2
            preactivity = activity
                
                
        return ans

