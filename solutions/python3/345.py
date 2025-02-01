
class Solution:
    # 定义一个方法 reverseVowels，用于翻转字符串中的元音字母顺序
    
    def reverseVowels(self, s):
        # 创建包含所有元音的列表
        r = [c for c in s if c in "aeiouAEIOU"]
        
        # 使用生成器表达式构建新字符串，其中每个元音字符被从列表 r 中弹出并替换原来的非元音字符
        return "".join(c in "aeiouAEIOU" and r.pop() or c for c in s)
