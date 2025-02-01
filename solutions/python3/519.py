
class Solution:

    def __init__(self, n_rows: int, n_cols: int) -> None:
        """
        初始化类，设置行数和列数，并创建一个已使用位置的集合。
        
        :param n_rows: 行数 (int)
        :param n_cols: 列数 (int)
        """
        self.rows = n_rows
        self.cols = n_cols
        self.used = set()
    
    def flip(self) -> list:
        """
        随机返回一个未被使用的位置，位置以 [行 - 1, 列 - 1] 的形式返回。
        
        :return: 一个未被使用的随机位置 (list)
        """
        while True:
            r = random.randint(1, self.rows)  # 随机选择一个行号
            c = random.randint(1, self.cols)  # 随机选择一个列号
            if (r, c) not in self.used:  # 如果该位置未被使用，则跳出循环并返回
                self.used.add((r, c))
                return [r - 1, c - 1]
    
    def reset(self) -> None:
        """
        将已使用的位置集合清空，以便重新开始。
        
        :return: 无 (None)
        """
        self.used = set()
