
class Solution:
    # 定义一个求最大子数组和的Kadane算法函数
    def Kadane(self, arr, res=0, cur=0):
        # 遍历数组中的每个元素
        for num in arr:
            # 更新当前子数组的最大值
            cur = max(num, num + cur)
            # 记录到目前为止找到的全局最大子数组和
            res = max(res, cur)
        return res
    
    def kConcatenationMaxSum(self, arr: List[int], k: int, mod=10 ** 9 + 7) -> int:
        # 如果k大于1，则将数组拼接两次并计算Kadane最大子数组和
        # 同时考虑到连续k次拼接的情况，先计算出数组元素的总和，并取其中较大的值
        return ((k - 2) * max(sum(arr), 0) + self.Kadane(arr * 2)) % mod if k > 1 else self.Kadane(arr) % mod
