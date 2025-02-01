
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # 使用collections.defaultdict来存储元素及其个数，初始化系数为1
        dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0
        
        for c in formula[::-1]:
            if c.isdigit():
                # 如果是数字，则计算当前数字并加到计数中
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ")":
                # 如果是右括号，将系数压入栈，并更新当前系数为栈顶元素
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == "(":
                # 如果是左括号，弹出栈顶元素作为当前系数的除数
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                # 如果是大写字母，则初始化或更新元素名称，并将之前累积的元素个数存储到字典中
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ""
                i = cnt = 0
            elif c.islower():
                # 如果是小写字母，则继续构建当前元素名称
                elem += c
        
        # 将字典中的元素及其个数按照字母顺序输出，处理单个元素的情况
        return "".join(k + (str(v > 1 and v or "") or "") for k, v in sorted(dic.items()))
