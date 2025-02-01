
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        """
        判断数组A是否可以被分割为三个具有相同和的子数组
        
        中文注释：判断数组A是否可以被分割为三个具有相同和的子数组
        """
        tar = sum(A) // 3  # 计算目标值，即每个部分应具有的和
        """
        英文注释：Calculate the target value, which is the sum each part should have.
        """
        sm = cnt = 0
        for a in A:
            sm += a  # 累加当前元素的值到sm中
            if sm == tar:  # 当累加和等于目标值时
                sm = 0  # 重置累计和
                cnt += 1  # 计数器加一，表示找到一个满足条件的部分
        """
        中文注释：遍历数组A中的每个元素，并检查是否可以将其分割成三个具有相同和的子数组。
        英文注释：Iterate through each element in array A, and check if it can be divided into three parts with the same sum.
        """
        return cnt == 3  # 检查计数器cnt是否等于3
