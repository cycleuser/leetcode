
class Solution(object):
    def threeEqualParts(self, A):
        """
        :param A: List[int] -- 输入数组A
        :return: List[int] -- 返回两个分割点，使得分割后的三部分相等
        
        思路：
        1. 计算数组中1的总和sm
        2. 如果sm不能被3整除，则不可能分成三个相同的部分，返回[-1, -1]
        3. 否则，每个部分需要包含的1的数量为t = sm // 3
        4. 特殊情况：如果t为0，说明数组全为0，直接返回[0, len(A) - 1]
        5. 寻找1的位置作为分割点breaks，并确定各部分起始和结束位置
        6. 检查三部分是否相等，不等则返回[-1, -1]
        7. 最后判断分割点的有效性，无效则返回[-1, -1]，否则计算并返回结果
        
        示例：
        A = [0, 0, 1, 0, 0, 1, 0, 1]
        输出：[3, 6]
        """
        
        sm = sum(A)
        if sm % 3: 
            return [-1, -1]
        
        t = sm // 3
        if not t:
            return [0, len(A) - 1]
        
        breaks = [0] + [i for i, x in enumerate(A) if x]
        i1, j1, i2, j2, i3, j3 = breaks[1], breaks[t], breaks[t + 1], breaks[2 * t], breaks[2 * t + 1], breaks[3 * t]
        
        if not (A[i1: j1 + 1] == A[i2: j2 + 1] == A[i3: j3 + 1]):
            return [-1, -1]
        
        if i2 - j1 < len(A) - j3 or i3 - j2 < len(A) - j3:
            return [-1, -1]
        
        return [j1 + len(A) - j3 - 1, j2 + len(A) - j3]
