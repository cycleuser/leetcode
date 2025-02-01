
class Solution(object):
    # 搜索目标值在给定的读取器中，返回目标值的索引；如果未找到，则返回-1。
    def search(self, reader, target: int) -> int:
        # 初始化左右边界
        l, r = 0, 20000
        
        # 二分查找
        while l <= r:
            mid = (l + r) // 2
            response = reader.get(mid)
            
            # 根据比较结果调整左右边界
            if response > target:
                r = mid - 1
            elif response < target:
                l = mid + 1
            else:
                return mid
        
        # 如果未找到目标值，返回-1
        return -1
