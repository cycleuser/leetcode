
class Solution:
    # 定义一个类Solution，用于解决同构映射问题

    def anagramMappings(self, A, B):
        # 创建一个字典 ind，将B中的每个元素及其索引存储起来
        ind = {num: j for j, num in enumerate(B)}
        
        # 遍历A中的每一个元素，在ind中查找对应的索引并返回结果列表
        return [ind[num] for num in A]
        # 中文注释：遍历数组A，通过字典ind快速获取B中对应值的索引，并构建结果列表
