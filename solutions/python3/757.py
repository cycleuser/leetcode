
class Solution(object):
    # 定义一个类，用于解决区间问题

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 按照区间的结束位置进行排序
        intervals.sort(key=lambda k: k[1])
        
        # 用于存储最终的结果集
        solution = []
        
        for start, end in intervals:
            # 如果结果集中为空或者最后一个元素不小于当前区间的起始位置
            if not len(solution) or solution[-1] < start:
                # 添加两个满足条件的数到结果集中
                solution.append(end - 1)
                solution.append(end)
            # 如果结果集中的倒数第二个元素不小于当前区间的起始位置
            elif solution[-2] < start:
                # 只添加一个满足条件的数到结果集中
                solution.append(end)
        
        # 返回结果集的长度，即满足条件的最小整数对的数量
        return len(solution)
