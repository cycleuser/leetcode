
class Solution:
    # 定义一个类来解决问题

    def shortestWay(self, source: str, target: str) -> int:
        # 初始化计数器和源字符串索引位置
        cnt = i = 0
        
        # 遍历目标字符串中的每个字符
        for t in target:
            # 在源字符串中寻找当前的目标字符，从上一次找到的位置开始
            i = source.find(t, i)
            
            # 如果找不到该字符，则从源字符串的开头重新查找
            if i == -1:
                i = source.find(t, 0)
                
                # 如果在源字符串中也找不到目标字符，则返回-1表示无法匹配
                if i == -1:
                    return -1
                
                # 找到新起点后，重置索引位置并增加计数器
                cnt += 1
                i = 0
        
        # 返回最小路径次数加上一次初始匹配操作
        return cnt + 1
