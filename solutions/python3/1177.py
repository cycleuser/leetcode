
class Solution:
    # 初始化计数器列表，用于记录每个子串的字符出现次数
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnts = [{}]
        
        # 遍历字符串s，构建每个位置的字符计数字典
        for i, c in enumerate(s):
            cnts.append(dict(cnts[-1]))
            cnts[-1][c] = cnts[-1].get(c, 0) + 1
        
        res = []
        
        # 遍历queries，检查每个子串是否可以通过修改最多k次字符变成回文
        for i, j, k in queries:
            # 计算在j+1位置的计数器中，与i位置计数器差异的字符次数，并减去k*2
            count_diff = sum((v - cnts[i].get(k, 0)) % 2 for k, v in cnts[j + 1].items()) - k * 2
            # 如果结果小于等于1，则可以变成回文，否则不能
            res.append(count_diff <= 1)
        
        return res
