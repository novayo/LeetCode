# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        '''
        1. get host name
        2. by host name, do bfs, we can cache url by set to prevent dulplicate queries
        '''
        def get_host_name(url):
            return url[7:].split('/')[0]
            
        host_name = startUrl[7:].split('/')[0]
        ans = []
        cache = set([startUrl])
        container = [startUrl]
        
        while container:
            target = container.pop()
            ans.append(target)
            
            for url in htmlParser.getUrls(target):
                if url not in cache \
                   and get_host_name(url) == host_name:
                    
                    container.append(url)
                    cache.add(url)
        return ans
        
# Input:
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com",
#   "http://news.yahoo.com/us"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = "http://news.yahoo.com/news/topics/"
# Output: [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.yahoo.com/us"
# ]
