
class Solution:
    # 计算小于n的质数个数
    def countPrimes(self, n):
        """
        :param n: int - 需要计算小于该值的质数个数
        :return: int - 小于n的质数个数

        优化点：使用埃拉托斯特尼筛法来更高效地找出所有质数。
                原代码错误在于对每个i都去掉了非质数，且方法不正确。

        新方案：遍历2到sqrt(n)之间的数字，如果当前数是质数，则将它的倍数标记为合数。
        """
        
        # 如果n小于2，直接返回0
        if n < 2:
            return 0

        # 初始化一个布尔数组，用于标记每个索引的值是否为质数
        is_prime = [True] * n
        p = 2
        
        while p * p < n:
            # 如果is_prime[p]没有被标记为False，则p是质数
            if is_prime[p]:
                # 标记p的倍数为合数
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1

        # 统计数组中True的数量，即质数个数
        return sum(is_prime)
