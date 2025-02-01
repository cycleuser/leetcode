
class Solution:
    def pushDominoes(self, dominoes):
        """
        解决推多米诺骨牌问题，给定一个字符串表示初始状态的多米诺骨牌序列。
        0. 定义结果字符串res和存储左右边界信息的字典l, r
        1. 遍历dominoes正向填充r字典记录右边界距离
        2. 反向遍历dominoes填充l字典记录左边界距离
        3. 根据规则确定结果字符串中的每个字符
        """
        res, l, r, pre_l, pre_r = "", {}, {}, None, None

        # 正向遍历填充r字典，记录每个点右侧最近的R的位置及距离
        for i, s in enumerate(dominoes):
            if s == "." and pre_r is not None: 
                r[i] = i - pre_r
            elif s == "R": 
                pre_r = i
            elif s == "L": 
                pre_r = None

        # 反向遍历填充l字典，记录每个点左侧最近的L的位置及距离
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == "." and pre_l is not None: 
                l[i] = pre_l - i
            elif dominoes[i] == "L": 
                pre_l = i
            elif dominoes[i] == "R": 
                pre_l = None

        # 根据规则确定结果字符串中的每个字符
        for i, s in enumerate(dominoes):
            if s == "L" or s == "R":
                res += s
            elif i in l and i in r:
                if l[i] < r[i]: 
                    res += "L"
                elif r[i] < l[i]: 
                    res += "R"
                else: 
                    res += s
            elif i in l: 
                res += "L"
            elif i in r: 
                res += "R"
            else: 
                res += s

        return res
