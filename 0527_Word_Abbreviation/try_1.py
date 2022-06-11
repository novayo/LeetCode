class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.remain_words = 0
        self.isWord = False
        
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        '''
        直接建立trie即可        
        Trie中，如果有一分支 底下的文字個數=1，此時就可以來計算答案了 => 可以用dfs做到
        internetn: inter3n
        intension: inten3n
        intrusion: intr4n
        
        internal, interval,  => intern1l (沒有必要變)  <= 要小心這個
        internal, interval
        '''
        indices = {}
        group = collections.defaultdict(list)
        for i, word in enumerate(words):
            group[word[0], word[-1], len(word)].append(word)
            indices[word] = i
        
        ans = [""] * len(words)
        for _, word_list in group.items():
            self.helper(word_list, ans, indices)
            
        return ans
    
    def helper(self, words, ans, indices):
        # add into trie
        trie = Node()
        for word in words:
            root = trie
            for w in word:
                root.remain_words += 1
                root = root.children[w]
            root.isWord = True
        
        # bfs
        que = collections.deque()
        for w, node in trie.children.items():
            que.append((w, node))
        
        ret = {}
        while que:
            w, node = que.popleft()
            
            # 這時候要去判斷底下的剩下字母還有誰
            if node.remain_words == 1:
                remain = ""
                while node.children:
                    _w = list(node.children.keys())[0]
                    remain += _w
                    node = node.children[_w]
                
                if len(remain) <= 2:
                    ret[w+remain] = w + remain
                else:
                    ret[w+remain] = w + f"{len(remain)-1}{remain[-1]}"
            
            # 如果還有超過一個字，那就加入que
            else:
                for _w, _n in node.children.items():
                    que.append((w+_w, _n))
        
        for string, abbrev in ret.items():
            ans[indices[string]] = abbrev
        
