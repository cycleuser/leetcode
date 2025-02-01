
class Solution:
    # 定义一个方法countAndSay，接收一个整数n作为参数
    def countAndSay(self, n):
        # 初始字符串设为"1"
        curr = "1"
        
        # 循环n-1次以生成第n个序列
        for i in range(n - 1):
            tmp, cnt = "", 1
            
            # 遍历当前字符串curr中的每一个字符
            for j, c in enumerate(curr):
                if j > 0 and curr[j - 1] == c: 
                    # 如果当前字符与前一个字符相同，计数加一
                    cnt += 1
                elif j > 0: 
                    # 否则将上一段的数字和字符添加到临时字符串tmp中，并重置计数器
                    tmp += str(cnt) + curr[j - 1]
                    cnt = 1
                
                if j == len(curr) - 1: 
                    # 遍历完当前字符串后，将最后一段的数字和字符也添加到临时字符串tmp中
                    tmp += str(cnt) + curr[j] 
            
            # 更新当前字符串为生成的新字符串
            curr = tmp
        
        # 返回最终结果
        return curr
