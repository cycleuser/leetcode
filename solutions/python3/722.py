
class Solution:
    def removeComments(self, source):
        # 初始化结果列表，块注释标志，当前行是否在注释中以及块注释开始位置
        res, block, cont, blockStart = [], False, False, -1
        
        for line in source:  # 遍历每一行代码
            if not cont: cache = ""  # 如果当前行不是在多行字符串中，则初始化缓存
            
            for i, c in enumerate(line):  # 遍历当前行中的每个字符
                if not block: 
                    cache += c  # 当前不在块注释中，将字符添加到缓存
                
                if cache[-2:] == "//":  # 如果缓存的最后两个字符是单行注释
                    cache = cache[:-2]  # 去掉注释部分并跳出循环
                    break

                elif cache[-2:] == "/*": 
                    blockStart, cache, block = i, cache[:-2], True  # 找到块注释开始位置，更新缓存和块注释标志
                
                elif line[i - 1:i + 1] == "*/" and blockStart < i - 1:  
                    # 如果找到块注释结束符且起始位置已确定
                    block = False  # 结束块注释状态

            if not block: 
                # 当前行没有在多行字符串中，将缓存添加到结果列表中
                if cache: res += cache,
            
            else:  # 如果当前行在多行字符串中，则保持状态并重置块注释开始位置
                cont, blockStart = True, -1

        return res  # 返回处理后的代码列表
