
class Solution:
    # 定义一个类来解决问题

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # 计算最小转动次数，使得数组A和B可以通过翻转使其所有元素相等
        
        res = min(len(A) - max(A.count(c), B.count(c)) if all(a == c or b == c for a, b in zip(A, B)) else float('inf')
                  for c in (A[0], B[0]))
        
        # 如果res小于无穷大，返回res，否则返回-1
        return res if res < float('inf') else -1
