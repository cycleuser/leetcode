
class Solution:
    # 定义一个类来解决最大交换问题

    def maximumSwap(self, num):
        # 将输入数字转换为列表，方便操作
        res, num = num, list(str(num))
        
        # 遍历数字的每一位，寻找最大的交换机会
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[i]):
                    # 构建新的数字，并与当前最大值比较
                    tmp = int("".join(num[:i] + [num[j]] + num[i + 1:j] + [num[i]] + num[j + 1:]))
                    if tmp > res:
                        res = tmp
        
        return res  # 返回最终的最大交换结果

