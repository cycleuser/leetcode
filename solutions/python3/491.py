
class Solution:
    # 定义一个类来解决寻找所有非递减子序列的问题

    def findSubsequences(self, nums):
        # 初始化结果集，包含空元组作为起点
        subs = {()}
        
        # 遍历输入的数字列表
        for num in nums:
            # 通过集合操作更新结果集，确保每个新元素仅添加到适当位置
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        
        # 过滤并返回长度大于等于2的非递减子序列列表
        return [sub for sub in subs if len(sub) >= 2]
