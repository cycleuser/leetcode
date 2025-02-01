
class Solution:
    # 计算分子和分母
    def fractionAddition(self, e: str) -> str:

        # 解析字符串中的一个分数片段
        def calc(i):
            l, r = i - 1, i + 1
            while l > 0 and e[l - 1].isdigit():
                l -= 1
            while r < len(e) - 1 and e[r + 1].isdigit():
                r += 1
            # 处理负号情况
            l = -int(e[l:i]) if l > 0 and e[l - 1] == "-" else int(e[l:i])
            r = int(e[i + 1:r + 1])
            return l, r
        
        # 计算最小公倍数 (LCM)
        def lcm(x, y):
            lcm = max(x, y)
            while True:
                if not lcm % x and not lcm % y:
                    return lcm
                lcm += 1
                
        # 计算最大公约数 (GCD)
        def gcd(x, y):
            for i in range(min(x, y), 0, -1):
                if not x % i and not y % i:
                    return i
                
        n = d = None
        for i in range(len(e)):
            if e[i] == "/":
                if n:
                    n2, d2 = calc(i)
                    newD = lcm(d, d2)
                    # 计算新的分子和分母
                    newN = n * (newD // d) + n2 * (newD // d2)
                    if newN:
                        r = gcd(abs(newD), abs(newN))
                        n, d= newN // r, newD // r
                    else:
                        n, d = 0, 1
                else:
                    # 处理第一个分数
                    n, d = calc(i)
        return str(n) + "/" + str(d)
