    
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """
        :type N: int          # 输入数字N的长度
        :type K: int          # 输入整数K，表示相邻两位间的差值
        :rtype: List[int]     # 返回符合条件的所有数字列表
        """
        q = {i for i in range(10)}  # 初始集合包含0到9的所有数字

        for _ in range(N - 1):  # 遍历N-1次，构造长度为N的数
            new = set()  # 新集合用于存储下一层可能的结果
            for num in q:  # 遍历当前层所有结果
                last = num % 10  # 获取当前数字的最后一位
                if num and 0 <= last + K <= 9:  # 检查加K是否合法
                    new.add(num * 10 + last + K)  # 将新构造的数字加入集合
                if num and 0 <= last - K <= 9:  # 检查减K是否合法
                    new.add(num * 10 + last - K)  # 将新构造的数字加入集合
            q = new  # 更新当前结果集为新的一层可能的结果

        return list(q)  # 转换并返回最终符合条件的所有数字列表
