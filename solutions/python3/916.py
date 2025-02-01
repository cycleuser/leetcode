
class Solution:
    # 定义一个类，用于解决单词子集问题

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 创建一个计数器对象，用于记录B中所有字符的最大出现次数
        cnt = collections.Counter()
        
        for b in B:
            # 对每个字符串b中的字符进行计数
            bc = collections.Counter(b)
            
            for k, v in bc.items():
                # 如果当前字符k在cnt中的值小于bc[k]，则更新cnt中k的值为bc[k]
                if cnt[k] < v:
                    cnt[k] = v
        
        res = []
        # 遍历A中的每个字符串a
        for a in A:
            # 检查cnt和当前字符串a组成的计数器之差是否为空，即a包含所有B中字符的最大出现次数
            if not (cnt - collections.Counter(a)):
                # 如果满足条件，则将a添加到结果列表中
                res.append(a)
        
        return res  # 返回结果列表
