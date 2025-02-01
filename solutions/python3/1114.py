
import threading

class Foo(object):

    def __init__(self):
        # 初始化两个信号量，分别用于控制 first 和 second 的执行顺序
        # two 用于确保 first 执行后 second 可以开始
        # three 用于确保 second 执行后 third 可以开始
        self.two = threading.Semaphore()
        self.three = threading.Semaphore()
        
        # 初始状态下两个信号量都被阻塞
        self.two.acquire()
        self.three.acquire()

    def first(self, printFirst: callable) -> None:
        """
        打印 "first" 的方法。
        :param printFirst: 用于打印 "first" 的方法，调用时会传入一个可调用对象
        :return: 无返回值
        """
        # 确保 first 先执行
        printFirst()
        
        # 发出信号，允许 second 执行
        self.two.release()

    def second(self, printSecond: callable) -> None:
        """
        打印 "second" 的方法。
        :param printSecond: 用于打印 "second" 的方法，调用时会传入一个可调用对象
        :return: 无返回值
        """
        
        # 等待 first 完成后执行 second
        self.two.acquire()
        
        # 打印 "second"
        printSecond()
        
        # 发出信号，允许 third 执行
        self.three.release()

    def third(self, printThird: callable) -> None:
        """
        打印 "third" 的方法。
        :param printThird: 用于打印 "third" 的方法，调用时会传入一个可调用对象
        :return: 无返回值
        """
        
        # 等待 second 完成后执行 third
        self.three.acquire()
        
        # 打印 "third"
        printThird()
