
class Solution:
    # 中文注释：定义一个类来解决字符串分组问题
    # 英文注释: Define a class to solve the anagram grouping problem

    def groupAnagrams(self, strs):
        from collections import defaultdict  # 中文注释：导入defaultdict以简化字典的使用；英文注释: Import defaultdict for easier dictionary handling
        
        dic = defaultdict(list)  # 中文注释：创建一个默认值为列表的字典来存储分组后的字符串；英文注释: Create a default dictionary with lists to store grouped strings

        for s in strs:
            key = ''.join(sorted(s))  # 中文注释：对每个字符串排序并合并成键；英文注释: Sort each string and join it to form the key
            dic[key].append(s)  # 中文注释：使用生成的键将原始字符串添加到对应的分组中；英文注释: Use the generated key to append the original string to its corresponding group

        return list(dic.values())  # 中文注释：返回字典中的所有值，即分组后的列表；英文注释: Return all values from the dictionary, which are the grouped lists
