
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        解决给定标签在之字形排序树中路径的问题。
        
        :param label: 标签值
        :return: 从根节点到该标签的路径列表
        """
        res = [label]  # 初始化结果列表，包含最终的目标标签
        
        while label != 1:
            """
            计算当前标签所在层数及偏移量，并更新当前标签。
            
            当前标签所在层：通过计算以2为底的对数得到
            偏移量：根据之字形排序树特性，计算相对于该层起始值的偏移量
            更新当前标签：通过公式重新计算父节点的标签值
            """
            d = int(math.log(label) / math.log(2))
            offset = int(2 ** (d + 1)) - label - 1
            label = (int(2 ** d) + offset) // 2
            
            # 将当前更新后的标签添加到结果列表的开头
            res = [label] + res
        
        return res  # 返回从根节点到目标标签的路径
