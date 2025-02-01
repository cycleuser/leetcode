
class Solution:
    # 该方法用于查找给定文本中，紧随在特定单词对之后的第三个单词
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # 将输入文本按空格分割成列表形式
        text = text.split()
        
        # 使用列表推导式找到满足条件的第三词，并返回结果列表
        return [text[i] for i in range(2, len(text)) if text[i-1] == second and text[i-2] == first]
