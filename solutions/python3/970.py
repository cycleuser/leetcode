
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        
        # 使用集合存储结果，避免重复值
        res = set()
        
        i, j = 0, 0
        
        # 对于x的幂次遍历
        while x ** i <= bound:
            # 对于y的幂次遍历
            while x ** i + y ** j <= bound:
                if (val := x ** i + y ** j) not in res:
                    res.add(val)
                
                j += 1
                
                # 如果y等于1，跳出内层循环
                if y == 1: 
                    break
            
            # 准备下一次x的幂次遍历
            j = 0
            i += 1
            
            # 如果x等于1，跳出外层循环
            if x == 1:
                break
        
        return list(res)
