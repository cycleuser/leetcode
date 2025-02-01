
class Solution:
    # 检查给定的数组是否为有效的山脉数组
    def validMountainArray(self, A):
        i = A and A.index(max(A))  # 找到数组中的最大值索引

        # 如果数组为空或只有一个元素，或者最大值在边界上，则不是有效山脉数组
        return (A and 
                0 < i < len(A) - 1 and  # 确保最大值不在边界且索引大于0和小于数组长度-1
                all(a1 < a2 for a1, a2 in zip(A[:i], A[1:i+1])) and  # 升序检查前半段
                all(a2 > a3 for a2, a3 in zip(A[i:], A[i+1:])) or False)  # 降序检查后半段
