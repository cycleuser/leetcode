
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        :param start: 起始基因序列 (Initial gene sequence)
        :param end: 目标基因序列 (Target gene sequence)
        :param bank: 可用的基因变异序列集合 (Set of available gene sequences for mutation)
        :return: 从起始基因到目标基因所需的最小变异次数，如果无法达到则返回-1 (Minimum number of mutations required to reach the target gene, or -1 if impossible)
        """
        
        bfs = [start]  # 使用广度优先搜索进行层级遍历
        genes = set(bank)  # 将可用的基因序列集合化以提高查找效率
        cnt = 0  # 记录变异次数

        while bfs:
            arr = []  # 用于存储当前层级可到达的新基因序列
            for g in bfs:
                if g == end:  # 如果当前基因序列为目标序列，返回当前的变异次数
                    return cnt
                for i, c in enumerate(g):  # 遍历当前基因序列中的每一个字符
                    for new in 'AGTC':  # 对于每个可能的新字符进行尝试
                        if new != c:  # 如果新字符与原字符不同
                            s = g[:i] + new + g[i + 1:]  # 构造新的基因序列
                            if s in genes:  # 如果该序列存在于可用的基因序列集合中
                                arr.append(s)  # 将其加入当前层级可到达的新序列列表
                                genes.discard(s)  # 并从集合中移除以避免重复访问

            bfs = arr  # 更新下一层级可访问的基因序列
            cnt += 1  # 变异次数加一
        
        return -1  # 如果没有找到目标序列，返回-1
