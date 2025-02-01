
class Solution:
    # 定义一个类来解决情侣座位交换问题

    def minSwapsCouples(self, row):
        """
        :param row: 初始的座位排列列表，表示每个座位编号
        :return: 最少需要交换的次数以使所有情侣成为邻居
        
        1. 初始化结果计数器 res 和索引字典 index
        2. 遍历座位数组 row 的偶数下标位置
            - 如果当前偶数编号的情侣不在正确的位置，进行以下操作：
                a) 找到需要交换的目标编号 f
                b) 交换当前情侣和目标情侣的座位，并更新索引字典
                c) 结果计数器 res 加一
        """
        res, index = 0, {num: i for i, num in enumerate(row)}  # 初始化结果计数器和索引字典
        
        for i in range(0, len(row), 2):  # 遍历偶数下标位置，确保每次处理两个座位
            if row[i] % 2 == 0 and row[i + 1] != row[i] + 1:  # 偶数编号的情侣不在正确的位置
                f = row[i + 1]
                row[i + 1], row[index[row[i] + 1]] = row[i] + 1, row[i + 1]  # 交换座位
                index[row[i] + 1], index[f] = i + 1, index[row[i] + 1]  # 更新索引字典
                res += 1  # 结果计数器加一
            
            elif row[i] % 2 != 0 and row[i + 1] != row[i] - 1:  # 奇数编号的情侣不在正确的位置
                f = row[i + 1]
                row[i + 1], row[index[row[i] - 1]], index[row[i + 1]] = row[i] - 1, row[i + 1], index[row[i] - 1]  # 交换座位并更新索引字典
                index[row[i] - 1], index[f] = i + 1, index[row[i] - 1]
                res += 1
        
        return res  # 返回最少交换次数
