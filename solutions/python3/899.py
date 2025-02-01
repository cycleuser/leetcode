
class Solution:
    # 定义有序队列类，用于解决字符串排序或旋转问题

    def orderlyQueue(self, S: str, K: int) -> str:
        # 如果K大于1，说明可以进行全排序
        if K > 1:
            # 返回已排序的字符串
            return "".join(sorted(S))
        
        # 否则K为1，只能通过旋转来尝试找到最小值
        else:
            # 生成所有可能的旋转子串并返回其中最小的一个
            return min(S[i:] + S[:i] for i in range(len(S)))
