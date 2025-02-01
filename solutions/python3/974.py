
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        计算数组A中和能被K整除的子数组数量
        
        Args:
            A (List[int]): 输入整数列表
            K (int): 整除的基数

        Returns:
            int: 和能被K整除的子数组数量
        """
        res = sm = 0  # 初始化结果和当前前缀和
        sums = collections.defaultdict(int)  # 使用字典存储前缀和出现次数
        sums[0] = 1  # 前缀和为0的情况初始化
        
        for a in A:  # 遍历输入数组A
            sm = (sm + a) % K  # 更新当前前缀和并对K取模
            sums[sm] += 1  # 当前前缀和出现次数加一
            res += sums[sm] - 1  # 累加满足条件的子数组数量
        
        return res  # 返回结果
