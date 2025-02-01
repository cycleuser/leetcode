
class Solution:
    # 中文注释：定义一个类Solution，用于实现字符串查找功能
    # 英文注释: Define a class Solution to implement string searching functionality
    
    def strStr(self, haystack: str, needle: str) -> int:
        # 中文注释：重载strStr方法，接受两个参数haystack和needle分别代表主字符串和子字符串
        # 英文注释: Override the strStr method which accepts two parameters: haystack and needle representing the main string and substring respectively
        
        return haystack.find(needle)  # 中文注释：使用内置find方法查找needle在haystack中的起始索引，返回结果
        # 英文注释: Use the built-in find method to search for the starting index of needle in haystack, and return the result
