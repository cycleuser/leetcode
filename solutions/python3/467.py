
class Solution:
    # 定义一个类用于解决寻找缠绕字符串中子串的问题

    def findSubstringInWraproundString(self, p):
        """
        :param p: str - 输入的字符串
        :return: int - 返回可以找到的最大缠绕子串数量
        
        解析输入字符串，统计每个字符作为结尾的最长缠绕子串长度。
        """
        
        res, l = {i: 1 for i in p}, 1
        # 初始化结果字典和当前子串长度

        for i, j in zip(p, p[1:]):
            # 遍历输入字符串，两两比较字符
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            # 判断是否构成缠绕序列，并更新当前子串长度

            res[j] = max(res[j], l)
            # 更新结果字典中每个字符的最大子串长度
        
        return sum(res.values())
        # 返回所有字符最大子串长度的总和
