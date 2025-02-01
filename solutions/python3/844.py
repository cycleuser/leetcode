
class Solution:
    # 比较两个字符串在执行删除操作后是否相等

    def backspaceCompare(self, S: str, T: str) -> bool:
        # 辅助函数：构建新字符串，忽略删除标记 '#'
        def construct(s: str) -> list[str]:
            new_s = []
            for c in s:
                if c == "#" and len(new_s) > 0:
                    new_s.pop()
                elif c != "#":
                    new_s.append(c)
            return new_s
        
        # 构造处理后的字符串
        s, t = construct(S), construct(T)
        
        # 比较两个构建后的字符串是否相等
        return s == t
