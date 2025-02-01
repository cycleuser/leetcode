
class Solution:
    # 定义一个方法，接收三个整数列表作为输入，并返回这三个列表中共有的元素列表
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # 使用集合求交集以去除重复值并利用短路逻辑减少不必要的比较
        return sorted(set(arr1) & set(arr2) & set(arr3))  # 返回排序后的交集元素列表
