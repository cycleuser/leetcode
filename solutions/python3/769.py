
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]     # 输入类型：整数列表
        :rtype: int               # 返回值类型：整数
        
        思路：
            - 遍历数组，维护已遍历最大值和计数器。
            - 当当前最大值等于已遍历元素数量减一时，表示可以分割一个有序块。
        """
        max_seen, total_seen, res_count = 0, 0, 0
        for num in arr:
            max_seen = max(max_seen, num)  # 更新已遍历中的最大值
            total_seen += 1                # 增加已遍历元素计数器
            
            if max_seen == total_seen - 1:  # 判断是否可以分割一个有序块
                res_count += 1              # 分割计数器加一
        
        return res_count                   # 返回可分块的数量
