
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # 初始化一个队列，用于存储当前生成的所有可能的字母变化组合
        bfs = ['']
        
        # 遍历输入字符串S中的每一个字符c
        for c in S:
            # 如果字符c是数字，则直接将其添加到所有已有组合之后
            if c.isdigit():
                bfs = [s + c for s in bfs]
            else:
                # 如果字符c是字母，则生成其大小写两种可能，并分别添加到已有组合之后
                bfs = [s + c.lower() for s in bfs] + [s + c.upper() for s in bfs]
        
        # 返回所有可能的字母变化组合
        return bfs
