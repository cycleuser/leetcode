
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        """
        :param S: 字符串S，表示排序顺序
        :param T: 字符串T，需要按S的顺序进行排序
        :return: 按照S中的顺序重新排列字符串T的结果
        """
        
        # 使用集合t保存字符串T中的所有字符，使用集合t2保存字符串S中的所有字符
        t = set(T)
        t2 = set(S)

        from collections import Counter as ct

        # 计算字符串T中每个字符的出现次数
        c = ct(T)

        # 根据S中的字符和它们在T中的出现次数生成按顺序排列的部分
        s = [char * c[char] for char in S if char in t]

        # 从T未出现在S中的字符中生成剩余部分
        add = [char * c[char] for char in t - t2]

        # 返回最终结果，即排序后的字符串
        return "".join(s + add)
