
class FreqStack:

    def __init__(self):
        """
        初始化类，使用defaultdict存储按频率分组的栈和计数器。
        :param: None
        """
        from collections import defaultdict, Counter
        self.stacks = defaultdict(list)
        self.freq = Counter()
        self.maxFreq = 0

    def push(self, x):
        """
        将元素x压入对应的频率栈中，并更新最大频率。
        :param x: 待添加的元素
        """
        self.freq[x] += 1 
        self.maxFreq = max(self.maxFreq, self.freq[x])
        self.stacks[self.freq[x]].append(x)

    def pop(self):
        """
        弹出并返回当前具有最大频率的栈中的最顶元素，更新计数器和最大频率。
        :return: 具有最大频率的栈中最顶元素
        """
        num = self.stacks[self.maxFreq].pop()
        self.freq[num] -= 1 
        if not self.stacks[self.maxFreq]: 
            self.maxFreq -= 1
        return num
