
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        中文注释：
        - 直接在原数组上操作，不返回任何值。
        - 遍历数组并处理0元素的复制逻辑。
        """

        i = 0
        for num in list(arr):
            if i >= len(arr): 
                break
            arr[i] = num
            if not num:
                i += 1
                if i < len(arr):
                    arr[i] = num
            i += 1
