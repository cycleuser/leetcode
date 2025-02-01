
class Solution:

    def __init__(self, N, blacklist):
        """
        初始化解决方案，设置禁止列表和相关参数

        :param N: 整数，表示范围的上限
        :param blacklist: 列表，包含禁止使用的数字
        """
        self.forbidden = set(blacklist)  # 将黑名单转换为集合以提高查找效率
        self.n = N                       # 总范围大小
        self.used = set()                # 已使用过的合法数字集合
        self.cur = 0                     # 当前尝试的数字

    def pick(self):
        """
        从允许范围内随机选择一个数字

        :return: 一个未被禁止且未使用的合法数字
        """
        while self.cur in self.forbidden:
            self.cur += 1  # 跳过禁止的数字

        if self.cur < self.n:
            num, self.cur = self.cur, self.cur + 1  # 选择当前合法的数并增加计数
        else:
            num = self.used.pop()  # 使用已使用过的合法数（若存在）
        
        self.used.add(num)  # 将选中的数字加入已使用集合
        
        return num
