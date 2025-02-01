
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        # 使用字典存储滑动窗口内出现的DNA序列及其频率，初始化时加入一个无效字符以简化边界处理
        dic, str = {}, "x" + s[:9]

        # 滑动窗口从第10个字符开始遍历到最后一个字符
        for i in range(9, len(s)):
            # 更新滑动窗口内的字符串，移除最左边的字符并添加当前字符
            str = str[1:] + s[i]
            # 根据字典更新频率或初始化为1
            dic[str] = 1 if str not in dic else dic[str] + 1

        # 返回所有出现超过一次的DNA序列
        return [k for k, v in dic.items() if v > 1]
