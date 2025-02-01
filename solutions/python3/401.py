
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int  # 输入的二进制数位数
        :rtype: List[str]  # 返回满足条件的时间列表

        构建一个从0到11的小时范围和0到59分钟范围，通过遍历组合小时和分钟，并检查其二进制表示中'1'的数量是否等于num。
        """
        return ['%d:%02d' % (h, m)
                for h in range(12)  # 遍历可能的小时值
                for m in range(60)  # 遍历可能的分钟值
                if (bin(h) + bin(m)).count('1') == num]  # 检查二进制表示中'1'的数量是否等于num
