
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        恢复给定字符串为有效的IP地址。
        
        :param s: 输入的字符串形式的数字序列
        :type s: str
        :return: 所有可能的有效IP地址列表
        :rtype: List[str]
        """

        if len(s) > 12:
            return []

        bfs = [(0, '')]  # 初始状态，当前位置为0，路径为空字符串

        for c in s:
            new = []
            c = int(c)
            for cur, st in bfs:
                # 如果当前数字加上新字符后的值小于等于255
                if cur * 10 + c <= 255 and (st[-1:] != '0' or cur):
                    new.append((cur * 10 + c, st + str(c)))  # 不加点的情况

                # 如果路径已非空，添加分隔符
                if st:
                    new.append((c, st + '.' + str(c)))  # 加上点的情况

            bfs = new  # 更新队列状态

        return [st for cur, st in bfs if st.count('.') == 3]  # 过滤出有效的IP地址（共4部分）
