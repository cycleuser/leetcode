
class Solution:
    # 定义一个方法用于查找下一个更大的数
    def nextGreaterElement(self, n: int) -> int:
        arr = [c for c in str(n)]  # 将整数转换为字符列表
        
        # 从右向左遍历数字的每一位，找到第一个满足arr[l] < arr[r]的位置l
        for l in range(len(arr) - 2, -1, -1):
            r = len(arr) - 1
            while l < r and arr[r] <= arr[l]:
                r -= 1  # 如果当前右边的数不大于左边的，则向左移动r指针
            
            if l != r:
                # 找到了可以交换的位置，进行交换，并对l之后的部分排序
                arr[l], arr[r] = arr[r], arr[l]
                arr[l + 1:] = sorted(arr[l + 1:])
                
                # 将字符列表转换回整数并返回，同时考虑溢出情况
                num = int("".join(arr))
                return num if -2 ** 31 <= num <= 2 ** 31 - 1 else -1
        
        # 如果没有找到更大数据，则返回-1
        return -1
