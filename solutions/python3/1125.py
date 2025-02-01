
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """
        解决问题：给定一系列需求技能和一些人员，每名人员拥有一部分技能。
                  找出最少人数的团队，使得该团队拥有所有所需技能。

        参数：
            - req_skills: 列表，表示所需的所有技能
            - people: 列表，每个元素是列表类型，表示每人掌握的技能集

        返回值：
            - 返回一个整数列表，表示组成最小需求团队的人员索引集合
        """
        
        n, m = len(req_skills), len(people)  # 总需求数量和人数
        
        key = {v: i for i, v in enumerate(req_skills)}  # 技能到索引的映射，提高查找效率
        dp = {0: []}  # 动态规划表初始化，key为技能集，value为对应人员集合

        for i, p in enumerate(people):
            his_skill = 0  # 当前人的技能状态表示
            
            for skill in p:
                if skill in key:  # 只考虑当前人已掌握的需求技能
                    his_skill |= 1 << key[skill]  # 使用位运算更新技能状态

            for skill_set, need in list(dp.items()):
                with_him = skill_set | his_skill  # 包含当前人的技能集合
                
                if with_him == skill_set: continue  # 若包含他后技能集不变则跳过
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    # 更新dp表，若新方案比旧方案更优或未记录则更新
                    dp[with_him] = need + [i]

        return dp[(1 << n) - 1]  # 返回拥有所有技能的最少人员组合
