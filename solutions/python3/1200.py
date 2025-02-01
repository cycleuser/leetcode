
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 对数组进行排序，以确保相邻元素之间的差值最小化
        arr.sort()
        
        # 计算相邻元素间的最小绝对差值
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        
        # 返回所有具有该最小绝对差值的相邻元素对
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]
