
class Solution:
    # Python 类定义

    def nthUglyNumber(self, n: int) -> int:
        # 初始化数组、堆和已使用过的数字集合
        arr, heap, used = [], [1], set()
        
        for i in range(n):
            # 从堆中弹出最小的丑数
            num = heapq.heappop(heap)
            arr.append(num)
            
            # 对于每个可能的因数（2、3、5），生成新的候选丑数并加入堆和已使用集合
            for p in (2, 3, 5):
                if p * num not in used:
                    heapq.heappush(heap, p * num)
                    used.add(p * num)
        
        # 返回第 n 个丑数
        return arr[-1]
