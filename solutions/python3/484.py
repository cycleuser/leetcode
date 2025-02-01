
class Solution:
    # 定义一个Solution类，包含findPermutation方法

    def findPermutation(self, s):
        # 初始化数组arr为长度为s+1的范围列表（从1到len(s)+2），cnt用于记录连续D的数量,n表示字符串s的长度
        arr, cnt, n = list(range(1, len(s) + 2)), 0, len(s)

        for i in range(n + 1):
            # 如果当前字符是"D"且还在范围内，增加计数器cnt
            if i < n and s[i] == "D":
                cnt += 1

            elif cnt:
                # 当遇到非"D"或到达字符串末尾时，反转cnt长度的数组段，并重置cnt为0
                arr[i - cnt:i + 1] = arr[i - cnt:i + 1][::-1]
                cnt = 0

        return arr  # 返回处理后的数组arr
