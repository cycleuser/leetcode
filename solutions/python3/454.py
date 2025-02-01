
from typing import List
import collections

class Solution:
    # 定义一个类来解决四数之和为零的问题
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 生成A和B的所有可能两数之和，并使用collections.Counter进行计数
        ab = collections.Counter([a + b for a in A for b in B])
        
        # 计算C和D所有可能两数之和的相反数在ab中出现的次数
        # 这里通过sum函数遍历C和D，检查其负值是否存在于ab中，并统计结果
        return sum(-c - d in ab and ab[-c-d] for c in C for d in D)
