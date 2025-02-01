
class Solution:
    """
    Given two arrays of integers 'gas' and 'cost', each representing the gas price 
    and cost to travel between stations respectively, this function determines if it's possible 
    to complete a circuit starting from one of the gas stations. If a solution exists, return the 
    index (starting station); otherwise, return -1.

    中文注释：
    给定两个整数数组 'gas' 和 'cost'，分别表示加油站的汽油价格和从一个加油站到下一个加油站的成本。此函数确定是否可以从某个加油站出发完成一圈。如果存在解决方案，则返回起始站的索引；否则，返回 -1。
    """

    def canCompleteCircuit(self, gas, cost):
        cur = 0
        index = 0

        # Iterate through each station to calculate the cumulative balance of fuel.
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            # If at any point the current balance goes below zero, reset it and start from the next station.
            if cur < 0:
                cur = 0
                index = i + 1

        # Check if a valid circuit can be completed starting from the identified station.
        return index if index < len(gas) and sum(gas) >= sum(cost) else -1
