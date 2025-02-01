
class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        使用字典记录状态，并找到循环节以优化计算。

        :param cells: 初始囚犯状态列表（字符串形式）
        :param N: 天数
        :return: N天后的囚犯状态列表（整数形式）
        """

        day, state, cur = 0, {}, "".join(map(str, cells))
        
        # 记录当前状态及其对应天数，直到遇到重复状态
        while cur not in state:
            state[cur] = day
            state[day] = cur
            if day == N:
                return list(map(int, cur))
            day += 1

            # 根据规则更新当天的囚犯状态
            cur = "0" + "".join(cur[i - 1] == cur[i + 1] and "1" or "0" for i in range(1, len(cur) - 1)) + "0"
        
        # 计算实际需要计算的天数，并返回结果
        return list(map(int, state[state[cur] + (N - state[cur]) % (day - state[cur])]))
