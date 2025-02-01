
import threading
from collections import deque

class BoundedBlockingQueue(object):
    # 初始化阻塞队列，设置容量上限
    def __init__(self, capacity: int):
        self.pushing = threading.Semaphore(capacity)  # 上限信号量
        self.pulling = threading.Semaphore(0)       # 下限信号量
        self.queue = deque()                        # 队列

    # 入队操作，阻塞直到有空余空间
    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.queue.append(element)
        self.pulling.release()

    # 出队操作，阻塞直到有元素可取
    def dequeue(self) -> int:
        self.pulling.acquire()
        self.pushing.release()
        return self.queue.popleft()

    # 返回当前队列大小
    def size(self) -> int:
        return len(self.queue)
