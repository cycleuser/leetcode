
class Solution:
    # 不返回任何内容，原地修改字符串列表s
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 遍历列表前半部分
        for i in range(len(s) // 2):
            # 交换位置i和对应的末尾元素-i-1
            s[i], s[-i-1] = s[-i-1], s[i]
