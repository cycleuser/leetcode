
class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]  # 输入参数，整数列表
        :rtype: int             # 返回最大环的长度
        """

        dic = {}  # 使用字典来记录每个元素访问过的次数

        for i in range(len(nums)):
            if i in dic:
                continue  # 如果当前索引已经处理过，则跳过

            j = i
            dic[j] = 1  # 初始化环的第一个节点的计数为1
            
            while nums[i] != j:  # 当未回到起始点时，继续循环
                dic[j] += 1      # 增加当前元素的访问次数
                i = nums[i]      # 更新索引到下一个元素位置
                dic[i] = 1       # 记录新节点被访问

        return max(dic.values())  # 返回所有环的最大长度
