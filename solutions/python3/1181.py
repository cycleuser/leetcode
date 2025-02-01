
class Solution:
    # 定义一个类来解决拼接谜题问题

    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        # 初始化结果列表
        res = []
        
        # 遍历每个短语对
        for i in range(len(phrases)):
            for j in range(i + 1, len(phrases)):
                # 获取第i个短语的最后一个单词
                w1 = phrases[i].split()[-1]
                # 获取第j个短语的第一个单词
                w2 = phrases[j].split()[0]

                # 如果两个相邻短语可以拼接
                if w1 == w2:
                    # 拼接并添加到结果中
                    r = phrases[i] + ' ' + ' '.join(phrases[j].split()[1:])
                    res.append(r.rstrip())

                # 交换i和j的角色，再次检查拼接可能性
                w1 = phrases[j].split()[-1]
                w2 = phrases[i].split()[0]

                if w1 == w2:
                    r = phrases[j] + ' ' + ' '.join(phrases[i].split()[1:])
                    res.append(r.rstrip())
        
        # 去重并排序结果
        return sorted(set(res))
