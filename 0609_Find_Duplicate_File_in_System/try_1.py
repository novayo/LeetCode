class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        '''
        paths[0]=
        'root/123 1.txt(123_123)'
        "root/d1/d2/jn/dm f1.txt(qweASD) f2.txt(f2_content) f3.txt(f3_content)"
        
        content一樣
        [
        ["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
        ["root/a/1.txt","root/c/3.txt"]]
        
        n = paths.length
        m = string.length in paths
        time comp.: n*m
        space comp.: n*m
        '''
        data = collections.defaultdict(list)
        
        for path in paths:
            splits = path.split(' ')
            root = splits[0]
            
            for path_file in splits[1:]:
                tmp = path_file.split('(')
                filename = tmp[0]
                content = tmp[1][:-1]
                data[content].append(root + r'/' + filename)
        
        ans = []
        for string, lists in data.items():
            if len(lists) >= 2:
                ans.append(lists)
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
