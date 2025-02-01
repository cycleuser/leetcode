
class Solution:
    # 将分数转换为小数形式
    def fractionToDecimal(self, n: int, d: int) -> str:
        # 根据符号决定结果是否需要加负号
        res = ["-"] if n * d < 0 else [""]
        n, d = abs(n), abs(d)
        
        # 整数部分的处理
        res.append(str(n // d))
        n %= d
        
        # 如果没有余数，直接返回结果
        if not n: 
            return "".join(res)
        
        # 小数部分开始
        res.append(".")
        
        # 使用哈希表记录出现循环的小数值及其位置
        mp = {n: len(res)}
        
        while n:
            n *= 10
            res.append(str(n // d))
            n %= d
            
            # 如果再次出现相同的余数，说明进入循环了
            if n in mp:
                res.insert(mp[n], "(")
                res.append(")")
                break
            
            # 更新哈希表记录当前余数的位置
            mp[n] = len(res)

        return "".join(res)
