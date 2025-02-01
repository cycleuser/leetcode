
class Solution:
    # 定义一个解决方案类，用于解决下一个最接近的时间问题

    def nextClosestTime(self, time):
        # 将时间字符串转换为字符集，并按字典序排序后去掉最后一个元素
        t = sorted(set(time))[:-1]
        
        # 构建一个映射字典nex，其中key为字符集中的字符，value为其后面的那个字符（如果存在）
        nex = {a: b for a, b in zip(t, t[1:])}
        
        # 从右到左遍历时间字符串
        for i, d in enumerate(time[::-1]):
            if d in nex:
                # 如果当前字符有下一个可用的字符替换
                
                if i == 0:
                    # 如果当前是秒位，则直接替换为nex[d]并返回结果
                    return time[:4] + nex[d]
                elif i == 1 and nex[d] < '6':
                    # 如果当前是分钟十位，且下一个可用的字符小于'6'，则替换为nex[d]并补上最小的小时位
                    return time[:3] + nex[d] + t[0]
                elif i == 3 and int(time[0] + nex[d]) < 24:
                    # 如果当前是分钟个位且替换后的时间小于24，则替换为nex[d]并保持原小时位不变
                    return time[0] + nex[d] + ':' + t[0] * 2
        
        # 若未找到合适替换，返回最小的合法时间
        return t[0] * 2 + ':' + t[0] * 2
