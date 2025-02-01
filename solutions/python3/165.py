
class Solution:
    # 定义辅助函数，解析字符串中的数字部分和剩余部分
    def getNum(self, s):
        """
        :param s: str 要解析的版本号字符串
        :return: tuple(剩余部分, 解析出的整数)
        """
        if not s:
            return (None, None)
        
        for i in range(len(s)):
            if s[i] == ".":
                # 找到小数点，返回剩余部分和解析出的整数
                return (s[i + 1:], int(s[:i]))
        
        # 如果没有找到小数点，则返回整个字符串转换后的整数
        return (None, int(s))

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        :param version1: str 第一个版本号字符串
        :param version2: str 第二个版本号字符串
        :return: int 比较结果 -1、0、1 分别表示版本2小于等于/等于/大于版本1
        """
        
        while True:
            # 解析version1，获取剩余部分和解析出的整数
            version1, n1 = self.getNum(version1)
            
            # 解析version2，获取剩余部分和解析出的整数
            version2, n2 = self.getNum(version2)

            # 如果两字符串均解析完毕且无数字部分，则返回0
            if version1 == version2 == n1 == n2 == None:
                return 0
            
            # 如果version1有非零数值且大于version2对应的数值或version2为空，返回1
            if (n1 != None and n1 > 0) and (n2 == None or n1 > n2):
                return 1

            # 如果version2有非零数值且大于version1对应的数值或version1为空，返回-1
            if (n2 != None and n2 > 0) and (n1 == None or n2 > n1):
                return -1
