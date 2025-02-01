
class Solution:
    # 定义一个类来解决最大子数组长度问题

    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        # 初始化索引字典、当前和以及结果长度
        index, sm, l = {}, 0, 0
        # 将初始和为0的索引设为-1
        index[0] = -1
        
        for i, num in enumerate(nums):
            # 累加当前元素值到总和
            sm += num
            
            # 如果当前和减去k在字典中存在，更新最大长度
            if (sm_k := sm - k) in index:
                l = max(l, i - index[sm_k])
            
            # 将当前和对应的索引加入字典（避免重复计算）
            if sm not in index:
                index[sm] = i
        
        return l  # 返回最大子数组长度
