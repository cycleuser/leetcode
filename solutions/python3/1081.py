
class Solution:
    # 定义一个解决类，用于寻找字符串中最短的子序列

    def smallestSubsequence(self, S: str) -> str:
        # 创建一个字典来记录每个字符最后出现的位置
        last = {c: i for i, c in enumerate(S)}
        
        res = ""  # 初始化结果字符串
        left = 0  # 左指针初始化为0
        
        while last:  # 当last字典不为空时，继续循环
            right = min(last.values())  # 找到last中最小的索引值
            
            # 寻找左区间[left, right]内的最左侧且不在结果字符串中的字符及其索引
            c, i = min((S[i], i) for i in range(left, right + 1) if S[i] not in res)
            
            left = i + 1  # 更新左指针为当前字符的下一个位置
            
            res += c  # 将找到的字符添加到结果字符串中
            
            del last[c]  # 从last字典中删除该字符以防止重复使用
        
        return res  # 返回最终的结果字符串
