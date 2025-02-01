
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        """
        构造给定字符串S中最大值的特殊序列。
        
        参数：
            S (str): 输入的原始字符串，只包含'0'和'1'
            
        返回：
            str: 通过递归构造的最大化后的特殊序列
        """
        count = i = 0
        # 初始化结果列表
        res = []
        
        for j, v in enumerate(S):
            # 更新括号计数器
            if v == '1':
                count += 1
            else:
                count -= 1
            
            # 当计数器归零时，表示找到一个子序列
            if count == 0:
                # 递归构造内部子序列，并将其添加到结果列表中
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        
        # 对所有子序列排序（升序），然后反转，以获得最大值
        return ''.join(sorted(res)[::-1])
