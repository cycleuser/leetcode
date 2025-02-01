
class Solution(object):
    # 定义一个类来解决魔数字符串问题
    
    def magicalString(self, n):
        """
        :param n: int - 需要生成的魔数字符串长度
        :return: int - 魔数字符串中数字1的数量
        
        中文注释：
        1. 初始化计数器cnt，初始魔数字符串s为"1"，布尔值two用于交替添加字符2或1。
        2. 使用for循环生成魔数字符串直到长度达到n-1。
        3. 根据s[i]的值决定cnt加1，并在末尾添加相应数量的2或1。
        4. 更新boolean变量two以交替添加字符。
        5. 如果n为1，直接返回1；否则返回计数器cnt的结果。
        
        英文注释：
        1. Initialize a counter cnt, and the initial magical string s as "1", and boolean variable two to alternate adding '2' or '1'.
        2. Use a for loop to generate the magical string until its length reaches n-1.
        3. Based on the value of s[i], increment cnt by 1 and append the corresponding number of '2' or '1' at the end.
        4. Update boolean variable two to alternate between adding characters.
        5. If n is 1, directly return 1; otherwise, return the result of counter cnt.
        """
        cnt, s, two = 0, "1", True
        for i in range(n - 1):
            if s[i] == "1":
                cnt += 1
                s += "2" if two else "1"
            else:
                s += "22" if two else "11"
            two = not two
        return cnt if n != 1 else 1
