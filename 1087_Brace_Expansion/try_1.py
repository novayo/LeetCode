class Solution:
    def expand(self, S: str) -> List[str]:
        self.graph, self.len = {}, 0

        # get graph from S
        partS, tmp = [], re.compile("[{}]").split(S)
        while '' in tmp:
            tmp.remove('')
        print(tmp)
        for c in tmp:
            if ',' in c:
                self.len += 1
            else:
                self.len += len(c)
        
        for s in tmp:
            partS.append(s.split(','))
        if len(partS) == 1:
            return partS[0]
        for i, value in enumerate(partS):
            self.graph[i] = value
        
        
        # get ans from graph
        self.ans = []
        def dfs(string: str, index: int):
            if len(string) == self.len:
                self.ans.append(string)
                return
            for n in self.graph[index]:
                dfs(string + n, index+1)
            
        dfs("", 0)
        return sorted(self.ans)
