
class Solution:
    def findBlackPixel(self, picture: List[str], N: int) -> int:
        """
        找出由 'B' 构成的恰好有 N 列的黑色像素个数。
        
        参数:
            picture (List[str]): 二维列表表示的图片，其中'B'代表黑色像素
            N (int): 黑色像素所在列的数量
        
        返回:
            int: 满足条件的黑色像素总数
        """
        m, n, res = len(picture), len(picture[0]), 0

        for row in picture:
            # 统计当前行中'B'的数量
            r_cnt = row.count("B")
            if r_cnt != N:
                continue
            
            # 遍历每列，检查是否满足条件
            for j in range(n):
                if row[j] == "B":
                    col_cnt, same = 0, 1  # 初始化列中'B'计数和行相同计数
                    for i in range(m):
                        if picture[i][j] == "B":
                            col_cnt += 1
                            if picture[i] == row:
                                same += 1
                            else:
                                break
                    
                    # 判断是否满足条件：列中'B'数量等于行中'B'数量且所有对应行都相同
                    if r_cnt == col_cnt == same:
                        res += 1
        
        return res
