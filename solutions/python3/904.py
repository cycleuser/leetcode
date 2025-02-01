
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        """
        初始化结果和指针i为0，使用字典last记录每种水果最后出现的位置
        :param tree: 树形列表，表示树上的水果种类
        :return: 最大可收集的两种不同类型的水果的数量
        """
        res = i = 0
        last = collections.defaultdict(int)
        
        for j, val in enumerate(tree):
            # 当前已记录的不同类型水果数量大于2且当前水果未在字典中，更新指针位置
            if len(last) == 2 and val not in last:
                pre = min(last.values())
                i = pre + 1
                last.pop(tree[pre])
            
            # 更新当前水果的位置到字典last中
            last[val] = j
            
            # 计算以j为结尾的最大可收集的两种不同类型的水果数量，更新结果res
            res = max(res, j - i + 1)
        
        return res
