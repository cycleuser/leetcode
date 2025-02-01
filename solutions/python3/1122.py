
class Solution:
    # 定义相对排序数组方法，接收两个整数列表作为输入并返回一个新列表
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 对arr1进行排序，key函数根据arr2中元素的索引位置或不在arr2中的情况下使用len(arr2) + x作为键值
        return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else len(arr2) + x)
