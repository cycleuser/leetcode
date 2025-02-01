
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        :param words: 一个单词列表
        :return: 返回所有可能的正方形单词组合
        """
        
        from collections import defaultdict
        
        # 使用defaultdict存储前缀及其对应的所有单词集合，以加快查找速度
        pref = defaultdict(set)
        
        for w in words:
            # 构建每个单词的所有长度的前缀，并添加到相应的前缀集合中
            for i in range(len(w)):
                pref[w[:i + 1]].add(w)
        
        def dfs(i: int, arr: List[str]) -> None:
            """
            深度优先搜索函数，用于构建正方形单词组合
            
            :param i: 当前处理的行索引
            :param arr: 当前行已填入的单词列表
            """
            if i == len(arr[0]):
                # 所有单词均按规则填充完成，则添加结果集
                res.append(arr)
            else:
                # 获取当前列的候选单词集合
                next_words = pref["".join(row[i] for row in arr)]
                
                for w in next_words:
                    # 递归尝试添加下一个单词，并进入下一层搜索
                    dfs(i + 1, arr + [w])
        
        # 从每个单词开始，尝试构建正方形单词组合
        res = []
        for w in words:
            dfs(1, [w])
        
        return res
