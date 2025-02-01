
class Solution:
    # 判断给定的单词列表是否构成一个有效的词方阵

    def validWordSquare(self, words):
        # 遍历每一行（即每个单词）
        for j, row in enumerate(words):
            col = ""  # 初始化列字符串
            
            # 构建当前行对应的列
            for s in words:
                try:
                    col += s[j]  # 拼接字符到列字符串中
                except: 
                    break  # 如果超出范围，终止构建

            # 判断当前行是否与构建的列相等
            if row != col:
                return False
        
        return True  # 所有行都满足条件，则返回True
