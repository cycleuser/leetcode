
class RecentCounter:

    def __init__(self):
        """
        初始化滑动窗口，使用双端队列存储ping的时间戳。
        :return: None
        """
        from collections import deque
        self.queue = deque()

    def ping(self, t: int) -> int:
        """
        添加一个新时间戳t，并移除超出3000毫秒范围的旧时间戳，返回当前窗口中的元素个数。
        :param t: 新的时间戳
        :return: 当前有效ping的数量
        """
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
