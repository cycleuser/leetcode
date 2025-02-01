
import threading

class FooBar(object):
    def __init__(self, n):
        """
        初始化，n为循环次数，f和b是信号量，用于控制foo和bar的执行顺序。
        
        :param n: int 循环次数
        """
        self.n = n
        self.f = threading.Semaphore(1)  # foo信号量初始化为1
        self.b = threading.Semaphore(0)  # bar信号量初始为0，阻塞bar线程

    def foo(self, printFoo):
        """
        打印foo。当foo信号量可用时执行此方法。

        :param printFoo: method 输出"foo"
        """
        for i in range(self.n):
            self.f.acquire()  # 等待foo信号
            printFoo()  # 输出"foo"
            self.b.release()  # 发布bar信号

    def bar(self, printBar):
        """
        打印bar。当bar信号量可用时执行此方法。

        :param printBar: method 输出"bar"
        """
        for i in range(self.n):
            self.b.acquire()  # 等待bar信号
            printBar()  # 输出"bar"
            self.f.release()  # 发布foo信号
