
class Solution:
    # Python 解法 - 循环排列

    def circularPermutation(self, n: int, start: int) -> List[int]:
        """
        :param n: 整数，表示数组的长度（2^n）
        :param start: 开始的整数值
        :return: 返回一个从start开始的循环排列数组
        
        优化说明：
            - 使用列表推导式替代for循环以简化代码
            - 通过位运算生成循环排列结果，提高计算效率
        """
        return [start ^ i ^ i >> 1 for i in range(1 << n)]
