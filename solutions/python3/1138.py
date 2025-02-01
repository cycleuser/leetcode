
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 创建字母与坐标映射，en：创建字母到坐标映射
        ind = {s: [i // 5, i % 5] for i, s in enumerate(string.ascii_lowercase)}
        
        x = y = 0  # 初始化当前位置，en：初始化当前位置
        res = ""   # 初始化结果字符串，en：初始化结果字符串
        
        for c in target:
            xx, yy = ind[c]  # 获取目标字母的坐标，en：获取目标字母的坐标
            
            if yy < y:       # 如果目标位置在当前列左侧
                res += 'L' * (y - yy)  # 左移操作
            if xx > x:       # 如果目标行号大于当前行号
                res += 'D' * (xx - x)  # 下移操作
            if xx < x:       # 如果目标行号小于当前行号
                res += 'U' * (x - xx)  # 上移操作
            if yy > y:       # 如果目标列号大于当前列号
                res += 'R' * (yy - y)  # 右移操作
            
            res += '!'   # 到达目标后移动到下一个字符，en：到达目标后移动到下一个字符
            x, y = xx, yy  # 更新当前位置坐标，en：更新当前位置坐标
        
        return res  # 返回结果字符串，en：返回结果字符串
