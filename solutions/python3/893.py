
class Solution:
    # 定义一个类来解决特殊等价分组问题

    def numSpecialEquivGroups(self, A):
        # 计算字符串A中不同特殊等价分组的数量
        
        # 通过构建每个字符串的奇数和偶数组合，并对它们进行排序后拼接
        # 利用集合去重，得到的不同组合即为特殊等价分组数量
        return len(set("".join(sorted(s[0::2])) + "".join(sorted(s[1::2])) for s in A))
        # 中文注释：通过构建每个字符串的奇数和偶数组合，并对它们进行排序后拼接
        # 利用集合去重，得到的不同组合即为特殊等价分组数量
