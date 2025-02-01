
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        :type list1: List[str]
        :param list1: 第一个餐厅列表
        :type list2: List[str]
        :param list2: 第二个餐厅列表
        :rtype: List[str]
        :return: 同时出现在两个列表中且索引和最小的餐厅名称列表
        """
        
        # 创建字典存储公共餐厅及其总索引值
        dic = {}
        for item1 in list1:
            if item1 in list2:  # 直接检查是否在第二个列表中，减少不必要的比较
                dic[item1] = list1.index(item1) + list2.index(item1)
        
        # 找到最小索引和对应的餐厅名称
        min_index_sum = min(dic.values())
        return [k for k, v in dic.items() if v == min_index_sum]
