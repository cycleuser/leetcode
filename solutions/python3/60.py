
class Solution:
    # 定义一个类，用于生成全排列

    def getPermutation(self, n: int, k: int) -> str:
        # 使用itertools.permutations生成1到n的数字的所有全排列
        p = itertools.permutations(range(1, n + 1))
        
        # 循环k次获取第k个排列
        for _ in range(k - 1):
            next(p)
            
        # 获取并返回第k个排列，转换为字符串形式
        res = next(p)
        return ''.join([str(i) for i in res])
