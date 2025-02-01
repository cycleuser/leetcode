
class Solution:
    # 定义一个类来解决问题
    
    def findShortestSubArray(self, nums):
        """
        :param nums: 列表形式的整数数组 (List[int])
        :return: 返回包含最短连续子数组的长度 (int)
        
        例如：输入 [1,2,2,3,1]，输出为 2。
              因为[2,2]是具有最大频率且最小长度的连续子数组
        """
        
        from collections import Counter, defaultdict
        
        # 使用Counter计算每个元素出现的次数
        cnt = Counter(nums)
        
        # 使用defaultdict来存储每个元素所有索引的位置
        seen = defaultdict(list)
        
        # 找到数组中的最大频率
        degree = max(cnt.values())
        
        # 将每个元素的所有索引位置存入seen中
        for i, v in enumerate(nums):
            seen[v].append(i)
        
        # 返回具有最大频率的子数组最小长度
        return min(seen[v][-1] - seen[v][0] + 1 for v in cnt if cnt[v] == degree)
