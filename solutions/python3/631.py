
class Excel(object):

    # 构造函数，初始化Excel表格，H为行数，W为列数（字母表示）
    def __init__(self, H, W):
        self.M = [[{'v': 0, 'sum': None} for i in range(H)] for j in range(ord(W) - 64)]

    # 设置单元格值
    def set(self, r, c, v):
        self.M[r - 1][ord(c) - 65] = {'v': v, 'sum': None}

    # 获取单元格的计算结果，优先返回直接设置的值，否则进行累加求和
    def get(self, r, c):
        cell = self.M[r - 1][ord(c) - 65]
        if not cell['sum']: return cell['v']
        return sum(self.get(*pos) * cell['sum'][pos] for pos in cell['sum'])

    # 设置单元格的计算公式，返回计算结果
    def sum(self, r, c, strs):
        self.M[r - 1][ord(c) - 65]['sum'] = self.parse(strs)
        return self.get(r, c)

    # 解析字符串为二维坐标集合
    def parse(self, strs):
        c = collections.Counter()
        for s in strs:
            s, e = s.split(':')[0], s.split(':')[1] if ':' in s else s
            for i in range(int(s[1:]), int(e[1:]) + 1):
                for j in range(ord(s[0]) - 64, ord(e[0]) - 64 + 1):
                    c[(i, chr(j + 64))] += 1
        return c
