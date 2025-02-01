
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # 初始化变量：数组长度，哈希对存储，结果值初始化为0，一个集合用于快速查找元素是否存在
        n = len(A)
        pair = {}
        res = 0
        back = set()

        for i in range(n):
            # 将当前数字加入集合中
            back.add(A[i])
            j = i + 1
            mx = 2 * A[i]
            
            while j < n and A[j] < mx:
                # 检查前一个元素和当前元素组成的斐波那契数对是否在哈希表中
                if (A[j] - A[i], A[i]) in pair:
                    # 如果存在，则更新这对的值为原来的值加1
                    pair[(A[i], A[j])] = pair[(A[j] - A[i], A[i])] + 1
                else:
                    # 如果不存在，但当前两个元素之差在集合中，初始化长度为3；否则初始为2
                    pair[(A[i], A[j])] = A[j] - A[i] in back and 3 or 2

                # 更新结果值为当前最大长度
                res = max(res, pair[(A[i], A[j])])
                j += 1
        
        # 返回结果，如果最长斐波那契子序列长度大于2，则返回该长度；否则返回0
        return res > 2 and res or 0
