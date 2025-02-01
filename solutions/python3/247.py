
class Solution:
    # 寻找所有n位的回文数（旋转对称数字）
    
    def findStrobogrammatic(self, n: int, q = [""]):
        # 生成长度为1到n-1的所有可能的前半部分
        for i in range(n // 2): 
            q = [s + c for s in q  for c in "01689" if i != 0 or c != "0"]
        
        # 如果n是奇数，需要在中间添加一个回文字符
        if n % 2: 
            q = [s + c for s in q for c in "018"]

        # 对生成的前半部分进行镜像拼接以形成完整的回文数
        for i in range(n // 2 - 1, -1, -1):  
            q = [s + "9" if s[i] == "6" else s + "6" if s[i] == "9" else s + s[i] for s in q]
        
        return q
