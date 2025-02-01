
class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        # 初始化两个指针和结果列表
        i = j = 0
        res = []
        
        # 双指针遍历A和B的区间
        while i < len(A) and j < len(B):
            # 计算重叠区间的起始和结束点
            s = max(A[i].start, B[j].start)
            e = min(A[i].end, B[j].end)
            
            # 如果有重叠区间，将其添加到结果中
            if s <= e:
                res.append(Interval(s, e))
                
            # 根据B区间的结束位置决定移动哪个指针
            if A[i].end < B[j].end:
                i += 1
            elif A[i].end == B[j].end:  # 两个区间同时结束的情况
                i += 1
                j += 1
            else:
                j += 1
        
        return res
