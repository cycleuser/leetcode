
class Solution:
    # 定义一个方法，计算将数组中所有1移至左侧所需的最小交换次数
    def minSwaps(self, data: List[int]) -> int:
        
        l = data.count(1)  # 统计数据中1的总数
        mn = cur = data[:l].count(0)  # 初始化当前窗口内0的数量
        
        for i in range(l, len(data)):
            # 滑动窗口更新：增加新元素并移除旧元素的影响
            cur += not data[i] 
            cur -= not data[i - l]
            
            # 更新最小交换次数
            mn = min(mn, cur)
        
        return mn  # 返回最小交换次数
