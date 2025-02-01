
class Solution:
    # 定义一个名为nextGreatestLetter的方法，接收两个参数：letters（有序字符列表）和target（目标字符）
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # 使用bisect模块的bisect函数在letters中查找大于等于target的第一个位置
        # 通过取模操作确保索引不会超出范围，返回该位置对应的字符
        return letters[bisect.bisect(letters, target) % len(letters)]
