# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        
        def condition(index):
            fontSize = fonts[index]
            
            height = fontInfo.getHeight(fontSize)
            
            if height > h:
                return False
            
            width = 0
            for t in text:
                width += fontInfo.getWidth(fontSize, t)
                
                if width > w:
                    return False
            
            return True
            
        
        
        ans = -1
        l, r = 0, len(fonts)-1
        
        while l <= r:
            mid = r - (r-l) // 2
            
            if condition(mid):
                ans = fonts[mid]
                l = mid+1
            else:
                r = mid-1
        
        return ans
                
