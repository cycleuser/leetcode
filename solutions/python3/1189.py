
class Solution:
    # 定义一个方法来计算字符串中最多可以组成多少个"balloon"
    
    def maxNumberOfBalloons(self, text: str) -> int:
        # 计算文本中每个关键字符出现的次数，并除以"balloon"中对应字符的数量
        return min(text.count(c) // 'balloon'.count(c) for c in 'ballo')
