
class Solution:
    # 定义一个名为Solution的类，包含用于解决问题的方法
    
    def lastStoneWeightII(self, A: List[int]) -> int:
        # 定义一个方法lastStoneWeightII，接收一个整数列表A作为参数，返回一个整数值

        dp = {0}
        # 初始化动态规划集合dp为只包含元素0的集合
        
        sumA = sum(A)
        # 计算输入列表A中所有元素之和，并存储在sumA变量中
        
        for a in A:
            # 遍历列表A中的每个元素a
            
            dp |= {a + i for i in dp}
            # 对于dp集合中的每一个i，计算a+i并将其添加到dp集合中
            # 使用对集操作（|）来合并两个集合，并将结果存储回dp
        
        return min(abs(sumA - i - i) for i in dp)
        # 返回集合dp中所有元素的两倍与sumA之差的绝对值中的最小值
