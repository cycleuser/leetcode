
class Solution:
    # 计算满足条件的连续整数序列数量
    def consecutiveNumbersSum(self, N):
        # 统计符合条件的数量
        cnt = 0
        
        # 遍历可能的差值d，范围从1到N
        for d in range(1, N + 1):
            # 计算当前差值下的总和与N的差异diff
            diff = d * (d - 1) // 2
            
            # 计算剩余需要补充的部分nd
            nd = N - diff
            
            # 如果剩余部分小于等于0，则结束循环
            if nd <= 0:
                break
            
            # 检查剩余部分是否能被当前差值整除，是则计数+1
            if nd % d == 0:
                cnt += 1
        
        return cnt
