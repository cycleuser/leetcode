
class Solution:
    def isNumber(self, s: str) -> bool:
        """
        判断字符串s是否为一个有效的数字。

        参数:
        s (str): 输入的字符串

        返回:
        bool: 如果s是有效数字则返回True，否则返回False
        """

        # 去除首尾空格
        s = s.strip()

        # 标记位：小数点是否出现过、e是否出现过、是否有数字以及e之后是否有数字
        point_seen, e_seen, number_seen, number_after_e = False, False, False, True

        for i, c in enumerate(s):
            if '0' <= c <= '9':
                # 数字字符，设置number_seen和number_after_e为True
                number_seen = number_after_e = True
            elif c == '.':
                # 小数点，检查之前是否已经出现过小数点或e
                if e_seen or point_seen:
                    return False
                point_seen = True
            elif c == 'e':
                # 指数符号e，检查之前是否已经出现过e或者没有数字
                if e_seen or not number_seen:
                    return False
                number_after_e = False  # e之后不再允许有小数点
                e_seen = True
            elif c in '-+':
                # 正负号，只能出现在首或e后第一个字符
                if i and s[i - 1] != 'e':
                    return False
            else:
                # 其他非法字符直接返回False
                return False

        # 最终检查是否所有条件都满足
        return number_seen and number_after_e
