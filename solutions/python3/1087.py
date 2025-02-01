
class Solution:
    # 定义一个类来解决排列问题

    def permute(self, S: str) -> List[str]:
        # 初始化队列，用于存储当前生成的字符串片段
        bfs = [""]
        # 标记是否需要处理多重字符
        mult = False
        # 临时列表用于存储待处理的多重字符
        chars = []
        
        for s in S:
            # 如果遇到逗号，跳过本次循环
            if s == ',':
                continue
            # 遇到左括号时，标记为需要处理多重字符
            elif s == '{':
                mult = True
            # 遇到右括号时，结束多重字符处理
            elif s == '}':
                # 对当前队列中的每个字符串片段与多重字符的每个字符进行组合
                bfs = [st + c for st in bfs for c in chars]
                # 重置临时列表和标记
                chars = []
                mult = False
            # 如果当前标志为真，说明是待处理的多重字符的一部分
            elif mult:
                chars.append(s)
            # 否则直接将字符添加到每个字符串片段后面
            else:
                bfs = [st + s for st in bfs]
        # 返回生成的所有合法排列，并按字典序排序
        return sorted(bfs)
