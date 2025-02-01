
class Solution:
    # 定义一个类用于处理排列问题

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        # 目标是找到前一个字典序的排列并进行一次交换
        
        pre = []
        for i in range(len(A) - 1, -1, -1):
            # 反向遍历数组A
            bisect.insort_left(pre, (A[i], i))
            # 将当前元素及其索引插入到有序列表pre中保持升序
            
            if pre.index((A[i], i)):
                # 如果当前元素在有序列表中有重复，则跳过
                j = pre[pre.index((A[i], i)) - 1][1]
                A[i], A[j] = A[j], A[i]
                # 找到前一个较小的元素并与其交换位置，以形成前一个字典序排列
                break
        return A
        # 返回修改后的数组
