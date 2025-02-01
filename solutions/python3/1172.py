
class DinnerPlates:

    def __init__(self, capacity: int):
        """
        初始化餐盘类，设置每个栈的容量capacity，并初始化空列表用于存储各个栈和可push与pop的栈索引。
        
        :param capacity: 每个栈的最大容量
        """
        self.c = capacity
        self.stacks = []
        self.l = []  # 可push的栈索引堆
        self.r = []  # 可pop的栈索引堆

    def push(self, val: int) -> None:
        """
        向可用栈中push值val。

        :param val: 要插入的整数值
        """
        if not self.l:
            # 如果当前没有可push的栈，则从右向左检查是否有空栈，如果存在则清空并记录为poppable。
            while self.r and not self.stacks[-self.r[0]]:
                heapq.heappop(self.r)
            i = 0 if not self.r else -self.r[0] + 1
            self.stacks.append([val])
            heapq.heappush(self.r, -i)
            # 如果当前栈容量未满，则记录为可push的栈。
            if len(self.stacks[i]) < self.c:
                heapq.heappush(self.l, i)
        else:
            i = self.l[0]
            # 尝试从可push的最左侧栈插入元素
            if not self.stacks[i]:
                heapq.heappush(self.r, -i)  # 如果该栈为空，则将索引记录为可pop的。
            self.stacks[i].append(val)
            # 如果当前栈已满，则更新可push的栈索引堆
            if len(self.stacks[i]) == self.c:
                heapq.heappop(self.l)

    def pop(self) -> int:
        """
        从当前栈中pop最上层元素，如果无可用栈则返回-1。
        
        :return: 被弹出的整数值，或-1表示没有可弹出的栈
        """
        while self.r and not self.stacks[-self.r[0]]:
            heapq.heappop(self.r)
        return self.popAtStack(-self.r[0]) if self.r else -1

    def popAtStack(self, index: int) -> int:
        """
        从指定栈index中pop最上层元素。

        :param index: 要操作的栈索引
        :return: 被弹出的整数值，若该索引无效或为空，则返回-1。
        """
        if index < len(self.stacks) and self.stacks[index]:
            ret = self.stacks[index].pop()
            # 如果当前栈仍有元素可push，则更新可push的栈索引堆
            if len(self.stacks[index]) == self.c - 1:
                heapq.heappush(self.l, index)
            return ret
        return -1
