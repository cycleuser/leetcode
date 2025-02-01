
class Solution:
    # 初始化字典和结果列表
    def letterCombinations(self, digits):
        # 中文注释：初始化字母映射字典和结果列表，初始值为一个空字符串
        dic, res = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}, ['']
        
        # 中文注释：遍历输入的每个数字
        for dig in digits:
            # 中文注释：临时列表，用于存储当前层的结果组合
            tmp = []
            
            # 中文注释：遍历当前结果列表中的每个字符串
            for y in res: 
                # 中文注释：遍历对应字母映射字典中的每个字符
                for x in dic[dig]: 
                    # 中文注释：将当前字符添加到字符串后，加入临时列表
                    tmp.append(y + x)
            
            # 更新结果列表为临时列表的内容
            res = tmp
        
        # 返回结果列表，如果为空则返回空列表
        return res if any(res) else []
