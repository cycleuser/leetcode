
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """
        判断queries中的每个字符串是否与pattern匹配。
        
        匹配规则：
        1. 每个queries中的字符顺序应与pattern中相同或在pattern的适当位置
        2. pattern中的所有小写字母必须出现在queries中对应的小写形式
        3. queries中出现的大写字母不能出现在pattern中
        
        参数:
            queries: 包含多个字符串的列表
            pattern: 模式字符串

        返回:
            结果列表，每个元素表示对应的query是否匹配pattern
        """
        res = []
        
        # 遍历queries中的每一个字符串
        for w in queries:
            j = 0
            
            # 遍历当前查询字符串w的每个字符c
            for c in w:
                # 如果当前模式字符和查询字符串字符相等，继续比较下一个模式字符
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                # 如果遇到大写字母，停止匹配（因为必须与pattern严格一致）
                elif c.isupper():
                    j = len(pattern) + 1
                    
            # 根据是否完全匹配模式字符串确定结果并添加至结果列表
            res.append(j == len(pattern))
            
        return res
