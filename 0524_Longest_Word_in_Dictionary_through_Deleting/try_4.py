class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        '''
        *1. sort dictionary by length and two pointer 
            => O(len(s) * n + nlogn) n for len(dictionary)
        
        
        fk this test case => after sort => still ["abe","abc"]
        "abce"
        ["abe","abc"]
        
        so do bucket sort instead
        
        
        2. do bfs to delete one char in every layer and find in dictionary(list to set) 
            => O(len(s)^2)
        '''
        buckets = collections.defaultdict(list)
        for string in dictionary:
            buckets[len(string)].append(string)
        
        for length in sorted(buckets.keys(), reverse=True):
            strings = sorted(buckets[length])
            
            for string in strings:
                ptr = 0
                for _s in s:
                    if _s == string[ptr]:
                        ptr += 1

                        if ptr >= len(string):
                            return string
        return ""
            
            
