
import threading


class ZeroEvenOdd:
    def __init__(self, n: int):
        """
        初始化方法，设置需要打印的数字数量n，并创建三个信号量：z（控制零）、e（控制偶数）、o（控制奇数）。
        初始时，e和o被锁定，确保首次执行的是zero方法。cur变量用于记录当前要打印的数值序号。
        """
        self.n = n
        self.z = threading.Semaphore()
        self.e = threading.Semaphore()
        self.o = threading.Semaphore()
        self.e.acquire()  # 初始锁定e信号量，保证首次执行的是zero方法
        self.o.acquire()  # 初始锁定o信号量，保证首次执行的是zero方法
        self.cur = 1

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        """
        打印零的方法。
        :param printNumber: Callable类型参数，用于打印数字。
        """
        for _ in range(self.n):
            self.z.acquire()
            printNumber(0)
            if self.cur % 2 == 1:
                self.o.release()  # 如果cur是奇数，则释放o信号量
            else:
                self.e.release()  # 如果cur是偶数，则释放e信号量

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        """
        打印偶数的方法。
        :param printNumber: Callable类型参数，用于打印数字。
        """
        for _ in range(self.n // 2):
            self.e.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.z.release()  # 打印完后释放z信号量，允许zero方法继续执行

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        """
        打印奇数的方法。
        :param printNumber: Callable类型参数，用于打印数字。
        """
        for _ in range(self.n // 2 + self.n % 2):
            self.o.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.z.release()  # 打印完后释放z信号量，允许zero方法继续执行
