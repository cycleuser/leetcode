
class Solution:
    # 中文注释：定义一个移除字符串中元音字母的方法
    def removeVowels(self, S: str) -> str:
        # 英文注释: Define a method to remove vowels from the given string
        return ''.join(filter(lambda x: x not in 'aeiou', S))
        
        # 中文注释：等价的另一种实现方式
        # 英文注释: Another equivalent implementation using list comprehension
        return ''.join(c for c in S if c not in 'aeiou')
