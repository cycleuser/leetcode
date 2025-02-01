
from threading import Lock

class H2O:
    """
    H2O class for simulating the production of water molecules (H2O).
    
    Attributes:
        H: Number of hydrogen atoms.
        O: Number of oxygen atoms.
        mu: Lock object to ensure thread safety.
    """

    def __init__(self):
        self.H = 0
        self.O = 0
        self.mu = Lock()  # 初始化锁以保证线程安全


    def hydrogen(self, releaseHydrogen):
        """
        Hydrogen function to simulate the addition of a hydrogen atom.

        :param releaseHydrogen: A function that releases a hydrogen atom.
        """
        with self.mu:
            self.H += 1
            self.output()


    def oxygen(self, releaseOxygen):
        """
        Oxygen function to simulate the addition of an oxygen atom.

        :param releaseOxygen: A function that releases an oxygen atom.
        """
        with self.mu:
            self.O += 1
            self.output()


    def output(self):
        """
        Output function to check and release atoms in pairs (H2 + O).
        """
        while self.ok():
            # 每次释放两个氢原子和一个氧原子形成水分子
            for _ in range(2):
                self.releaseHydrogen()
            self.releaseOxygen()
            self.H -= 2
            self.O -= 1


    def ok(self):
        """
        Check if there are enough hydrogen and oxygen atoms to form a water molecule.
        
        :return: True if H >= 2 and O >= 1, otherwise False.
        """
        return self.H >= 2 and self.O >= 1
