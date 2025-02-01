
class Solution:
    # 定义一个类，用于寻找数组中的缺失数字

    def missingNumber(self, arr: List[int]) -> int:
        """
        :param arr: 输入的整数列表
        :return: 缺失的数字
        
        该函数通过计算相邻元素之间的差值来确定缺失的数字。
        假设给定数组为 [a0, a1, ..., an]，且存在一个缺失的数字 x，则有：
            - 数组的第一个和最后一个元素之间应有一个等间距
            - 在遍历过程中，如果当前元素与前一个元素之间的差值不等于该等间距，则说明缺失的数字就在它们之间
        """
        d = (arr[-1] - arr[0]) // len(arr)  # 计算数组中相邻元素之间的预期差值
        
        for a, b in zip(arr, arr[1:]):
            if b != a + d:
                return a + d  # 返回缺失的数字
        return 0  # 如果没有找到，则返回0（假设缺失的是第一个元素）
