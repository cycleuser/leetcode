
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        :param input: 输入的字符串，包含多级目录结构信息（用换行符分隔）
        :return: 返回最长路径长度

        思路：通过分析每一行的缩进程度（depth）来确定文件或目录的位置
              使用字典pathlen存储每个深度级别的路径长度
        """
        
        maxlen = 0  # 最长路径长度
        pathlen = {0: 0}  # key为深度，value为该深度下的路径长度
        
        for line in input.splitlines():
            name = line.lstrip('\t')  # 去掉首部的制表符，得到文件或目录名称
            depth = len(line) - len(name)  # 计算缩进程度（depth）
            
            if '.' in name:  # 如果是文件
                maxlen = max(maxlen, pathlen[depth] + len(name))  # 更新最大路径长度
            
            else:  # 如果是目录
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1  # 更新下一层目录的路径长度
        
        return maxlen
