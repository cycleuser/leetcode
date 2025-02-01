
class Solution:
    # 寻找最长链路的方法，输入为一个二维数组pairs
    def findLongestChain(self, pairs):
        # 按照每对元素的第二个值排序
        pairs.sort(key=lambda x: x[1])
        
        # 初始化结果res和前一个元素的第二位值pre
        res, pre = 1, pairs[0][1]
        
        # 遍历pairs中的每个元素，从索引为1开始
        for c, d in pairs[1:]:
            # 如果当前元素的第一个值大于前一个元素的第二个值，则形成一个新的链路
            if pre < c:
                pre = d  # 更新pre为当前元素的第二个值
                res += 1  # 长度加一
        
        # 返回最长链路的长度
        return res
