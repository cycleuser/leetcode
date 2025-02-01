
class Solution:
    # 解决数字序列匹配问题，输入字符串S由'I'和'D'组成
    # 'I'表示当前数比前一个数大，'D'表示当前数比前一个数小
    
    def diStringMatch(self, S):
        l, r, arr = 0, len(S), []  # 初始化左指针l为0，右指针r为S的长度，结果数组arr为空
        for s in S:
            # 如果字符是'I'，则当前数比前一个数大，将其加入结果数组；否则将当前数设置为较小值
            arr.append(l if s == "I" else r)
            l, r = l + (s == "I"), r - (s == "D")  # 更新指针位置
        return arr + [l]  # 最后一个数字直接添加到结果数组尾部
