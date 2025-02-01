
class Solution:
    # 定义一个求解最长连续序列的方法
    def longestConsecutive(self, nums):
        # 将输入的nums转换为集合items，去重并提高查找效率
        res, items = 0, set(nums)
        
        for num in items:
            # 如果当前数字num-1不在集合中，则说明可以从num开始寻找最长连续序列
            if num - 1 not in items:
                cur = 1  # 当前连续序列的长度初始化为1
                while num + 1 in items: 
                    num, cur = num + 1, cur + 1   # 继续查找下一个连续数字并增加当前序列长度
                if cur > res: 
                    res = cur  # 更新结果，如果当前序列更长则替换result
        
        return res  # 返回最长的连续序列长度
