
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        :param people: 人重量列表
        :param limit: 每艘船的最大载重限制
        :return: 所需的最小船只数量
        """

        # 对人员重量进行排序，以便轻的人和重的人可以配对或单独乘坐
        people.sort()

        l, r, cnt = 0, len(people) - 1, 0
        # 双指针遍历列表
        while l <= r:
            if l != r and people[l] + people[r] > limit: 
                # 如果轻的人与重的人之和超过限制，移动右指针以尝试更轻的组合
                r -= 1
            else:
                # 否则，两人都可以乘坐一艘船
                l += 1
                r -= 1
            cnt += 1
        
        return cnt
