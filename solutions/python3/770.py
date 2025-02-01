
class Solution(object):
    def basicCalculatorIV(self, s: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        """
        :param s: 字符串表达式
        :param evalvars: 用于替换的变量名列表
        :param evalints: 对应evalvars中的整数值列表
        :return: 计算结果后的字符串表示形式
        """

        # 移除空格并初始化字典
        s.strip()
        d = dict(zip(evalvars, evalints))
        s = s.replace(' ', '')

        # 使用正则表达式拆分字符串
        ts = re.findall('\u005Cd+|[-()+*]|[^-()+*]+', s)

        # 向量加法函数
        def add(p: list[tuple[list[str], int]], q: list[tuple[list[str], int]]) -> list[tuple[list[str], int]]:
            """
            合并两个向量表达式，并进行必要的合并操作

            :param p: 第一个向量表达式
            :param q: 第二个向量表达式
            :return: 一个新的合并后的向量表达式列表
            """
            i, j = 0, 0
            r = []
            while i < len(p) and j < len(q):
                v, c = p[i]
                v2, c2 = q[j]
                if v == v2:
                    if c + c2 != 0:
                        r.append((v, c + c2))
                    i += 1
                    j += 1
                elif len(v) > len(v2) or (len(v) == len(v2) and v < v2):
                    r.append(p[i])
                    i += 1
                else:
                    r.append(q[j])
                    j += 1

            # 合并剩余部分
            r += p[i:]
            r += q[j:]
            return r

        # 向量取负函数
        def neg(p: list[tuple[list[str], int]]) -> list[tuple[list[str], int]]:
            """
            对向量表达式的系数取负数

            :param p: 输入的向量表达式列表
            :return: 取负后的向量表达式列表
            """
            r = []
            for v, c in p:
                r.append((v, -c))
            return r

        # 向量减法函数
        def sub(p: list[tuple[list[str], int]], q: list[tuple[list[str], int]]) -> list[tuple[list[str], int]]:
            """
            两个向量表达式的差值

            :param p: 第一个向量表达式列表
            :param q: 第二个向量表达式列表
            :return: 计算后的向量表达式列表
            """
            return add(p, neg(q))

        # 向量乘法函数
        def mult(p: list[tuple[list[str], int]], q: list[tuple[list[str], int]]) -> list[tuple[list[str], int]]:
            """
            两个向量表达式的乘积

            :param p: 第一个向量表达式列表
            :param q: 第二个向量表达式列表
            :return: 计算后的向量表达式列表
            """
            r = []
            for v, c in p:
                for v2, c2 in q:
                    r = add(r, [(sorted(v + v2), c * c2)])
            return r

        # 运算符优先级函数
        def prec(c: str) -> int:
            """
            根据运算符确定其优先级

            :param c: 一个字符，代表运算符
            :return: 该运算符的优先级
            """
            if c in [')']:
                return 0
            elif c in ['+', '-']:
                return 1
            else:
                return 2
        
        i = 0

        # 解析表达式函数
        def expr(p: int) -> list[tuple[list[str], int]]:
            """
            对表达式的解析和计算

            :param p: 当前的运算优先级
            :return: 计算后的向量表达式列表
            """
            nonlocal i, ts
            if ts[i] == '(':
                i += 1
                v = expr(0)
                i += 1
            elif ts[i] == '-':
                i += 1
                v = neg(expr(3))
            elif re.match('\u005Cd+', ts[i]):
                if ts[i] != '0':
                    v = [([], int(ts[i]))]
                else:
                    v = []
            else:
                if ts[i] in d:
                    if d[ts[i]] != 0:
                        v = [([], d[ts[i]])]
                    else:
                        v  = []
                else:
                    v = [([ts[i]], 1)]
            
            while i < len(ts) - 2 and prec(ts[i+1]) > p:
                op = ts[i+1]
                i += 2
                v2 = expr(prec(op))
                if op == '+': v = add(v, v2)
                if op == '-': v = sub(v, v2)
                if op == '*': v = mult(v, v2)
                
            return v

        # 将向量表达式转换为字符串形式
        def tostrings(p: list[tuple[list[str], int]]) -> list[str]:
            """
            将向量表达式列表转换成对应的字符串表示形式

            :param p: 向量表达式的列表
            :return: 对应的字符串列表
            """
            r = []
            for v, c in p:
                term = ' + '.join(['*'.join(v[::-1]) if len(v) > 0 else '' for v in [v]])
                r.append(f'{c} * {term}')
            
            return [''.join(r).strip('+ ')]

        # 返回最终计算结果
        return tostrings(expr(3))
