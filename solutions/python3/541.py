
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        :param s: 输入字符串
        :param k: 每段长度
        :return: 反转指定段落后的字符串
        """

        # 使用列表推导式，分段处理字符串
        return "".join([s[i:i + k][::-1] + s[i + k:i + 2 * k]
                        for i in range(0, len(s), 2 * k)])  # 每2k个字符为一段进行处理
