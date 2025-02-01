
class Solution:
    """
    解决方案类，用于实现计算最后剩余石块重量的方法。
    
    :param stones: List[int], 表示初始的石块列表
    :return: int, 返回最后剩下的石块的重量，如果为空则返回0
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        计算最后一颗剩余的石块的重量。

        方法逻辑：
        1. 首先对所有石块进行排序。
        2. 然后不断从列表中取出两个最大的石块，计算它们之间的差值并插入回原列表。
        3. 重复上述过程直到只剩下一个或没有石块为止。
        4. 返回剩余的石块重量。

        :param stones: List[int], 排序后的石块列表
        :return: int, 剩余石块的重量
        """
        stones.sort()  # 对石块进行排序

        for _ in range(len(stones) - 1):
            # 取出两个最大的石块，计算差值，并将差值插入回列表中
            diff = stones.pop() - stones.pop()
            bisect.insort(stones, diff)

        return stones[0] if stones else 0  # 返回剩余的石块重量，如果为空则返回0
