
class Solution:
    # 定义一个类用于解决交换字符串最小次数的问题

    def minimumSwap(self, s1: str, s2: str, xy: int = 0, yx: int = 0) -> int:
        """
        计算将s1和s2转换为完全相同的两个字符串所需的最少交换次数。

        参数:
            s1 (str): 第一个输入字符串
            s2 (str): 第二个输入字符串
            xy (int, optional): "x" 和 "y" 之间的互换计数. 默认为0。
            yx (int, optional): "y" 和 "x" 之间的互换计数. 默认为0。

        返回:
            int: 如果可以通过最少交换次数使两个字符串相同，则返回该次数，否则返回-1
        """
        
        # 使用zip函数将s1和s2的对应字符两两配对比较
        for a, b in zip(s1, s2):
            xy += a == "x" and b == "y"  # 如果当前字符匹配xy模式，则计数xy
            yx += a == "y" and b == "x"  # 如果当前字符匹配yx模式，则计数yx
        
        # 计算总交换次数和是否可以成功转换
        return (xy + yx) // 2 + (xy % 2) * 2 if xy % 2 == yx % 2 else -1
