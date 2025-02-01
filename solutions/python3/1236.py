
class Solution:
    # """
    # 这是HtmlParser的API接口。
    # 不需要实现该接口，也不应推测其实现方式。
    # """
    # class HtmlParser(object):
    #     def getUrls(self, url: str) -> List[str]:
    #         pass

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # 获取起始URL的主机名
        host = startUrl[:startUrl.find('/', startUrl.find('//') + 2)]
        
        # 初始化队列和已访问集合
        q, seen = [startUrl], {startUrl}
        
        # 遍历队列中的每个URL
        for url in q:
            # 获取当前URL的所有链接
            for nex in htmlParser.getUrls(url):
                # 检查链接是否属于同一主机且未被访问过
                if nex[:nex.find('/', nex.find('//') + 2)] == host and nex not in seen:
                    q.append(nex)
                    seen.add(nex)
        
        return q
