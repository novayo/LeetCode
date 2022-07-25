class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ''
        sorted_list = []
        for idx, source, target in zip(indices, sources, targets):
            sorted_list.append((idx, source, target))
        sorted_list.sort()
        
        current_idx = len(s)
        for idx, source, target in sorted_list[::-1]:
            end_idx = idx + len(source)
            if s[idx: end_idx] != source:
                continue
            
            ans = target + s[end_idx: current_idx] + ans
            current_idx = idx
        
        return s[: current_idx] + ans
