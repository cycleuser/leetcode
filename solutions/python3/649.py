
class Solution:
    def predictPartyVictory(self, senate):
        # 初始化R和D的禁用计数器
        ban_r = ban_d = 0
        
        # 循环直到胜负者确定
        while True:
            # 新一轮参议员列表
            new = []
            
            # R和D参议员的数量统计
            r_cnt = d_cnt = 0
            
            # 遍历当前参议院成员
            for s in senate:
                if s == 'R':
                    # 增加R计数，如果已禁用则减少禁用计数，否则增加D的禁用计数并移除R
                    r_cnt += 1
                    if ban_r > 0:
                        ban_r -= 1
                    else:
                        ban_d += 1
                        d_cnt -= 1
                        new.append(s)
                elif s == 'D':
                    # 增加D计数，如果已禁用则减少禁用计数，否则增加R的禁用计数并移除D
                    d_cnt += 1
                    if ban_d > 0:
                        ban_d -= 1
                    else:
                        ban_r += 1
                        r_cnt -= 1
                        new.append(s)
            
            # 判断胜负条件
            if d_cnt < 0 < r_cnt:
                return "Radiant"
            elif r_cnt < 0 < d_cnt:
                return "Dire"
            
            # 更新参议院成员列表
            senate = new
