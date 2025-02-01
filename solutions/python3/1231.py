
class Solution:
    # 定义一个辅助函数来检查是否可以将糖果分割成至少K+1份，每份的甜度不低于m
    def maximizeSweetness(self, sw: List[int], K: int) -> int:
        def ok(m):
            count = sum_ = 0
            for sweetness in sw:
                sum_ += sweetness
                if sum_ >= m:
                    sum_ = 0 
                    count += 1
            return count >= K + 1
        
        # 初始化二分查找的左右边界
        left, right = 1, sum(sw)
        
        # 使用二分查找来确定最大可能的最小甜度
        while left < right:
            mid = (left + right) // 2
            if ok(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        print(left, right)
        return right if ok(right) else left - 1
