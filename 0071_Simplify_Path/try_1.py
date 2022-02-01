class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        
        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            elif p == '..':
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(p)
                
        return '/' + '/'.join(path_stack)
