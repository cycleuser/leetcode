
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        # 初始化：B转换为列表形式，获取字符串长度n，初始化最小操作次数k为无穷大，
        #       并创建一个栈，初始元素包含索引0、当前计数0和复制的A
        b, n, k, stack = [c for c in B], len(A), float("inf"), [(0, 0, [c for c in A])]
        
        # 当栈非空时循环
        while stack:
            i, cnt, s = stack.pop()  # 弹出栈顶元素，包含当前索引、操作计数和字符串列表副本
            
            # 找到与B当前位置字符不同的第一个位置i
            while i < n and s[i] == b[i]:
                i += 1
            
            # 如果找到全部匹配，则更新最小操作次数k
            if i == n:
                if cnt < k:
                    k = cnt
                    
            else:
                # 寻找可以交换的位置j，满足条件：s[j] == b[i]且s[j] != b[j]
                for j in range(i + 1, n):
                    if s[j] == b[i] and s[j] != b[j]:
                        ls = s[:]  # 复制字符串列表副本
                        ls[i], ls[j] = ls[j], ls[i]  # 进行交换操作
                        
                        # 将新的索引、计数加1和更新后的列表压入栈中
                        stack.append((i + 1, cnt + 1, ls))
        
        return k  # 返回最小的操作次数k
