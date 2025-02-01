
class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        """
        定义一个类Solution，并在其中定义cheapestJump方法。
        该方法接收两个参数：A为一维数组，B为正整数。
        返回值是一个包含跳转路径的列表或空列表。
        
        英文注释：
        Define a class Solution and in it define the cheapestJump method.
        This method takes two parameters: A as a list of integers, B as a positive integer.
        It returns a list containing the path of jumps or an empty list.
        """
        
        n = len(A)
        # 初始化preMin字典，记录每个位置跳转的最小花费及其前一个位置
        preMin = {n - 1: [n]}
        
        for i in range(n - 2, -1, -1):
            if A[i] == -1:
                continue
            
            mn, preIndex = float("inf"), None
            # 遍历从当前位置到B步范围内，寻找最小花费及其前一个位置
            for ind in range(i + 1, min(i + B + 1, n)):
                if -1 < A[ind] < mn:
                    mn, preIndex = A[ind], ind
            
            # 如果找到了合适的前一个位置，则更新当前位置的花费和preMin字典
            if preIndex is not None:
                A[i] += A[preIndex]
                preMin[i] = preMin[preIndex] + [i + 1]
            else:
                # 如果没有找到合适的位置，说明无法从当前位置跳跃到目标位置
                A[i] = -1
        
        # 返回路径列表或空列表
        return (0 in preMin and preMin[0][::-1]) or []
