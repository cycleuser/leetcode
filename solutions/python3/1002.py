
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        创建一个字典cnt来存储每个字母在所有字符串中出现的最小次数和出现的字符串数量。
        初始化时，将字母'a'到'z'作为键，对应的值设置为无穷大（表示初始最大小于实际需求）和0（未出现过）。

        遍历输入列表A中的每个单词w，使用collections.Counter计算其字符频率，并更新字典cnt中对应字符的最小频次。
        同时记录该字符在哪些字符串中出现过了。
        
        最后遍历字典cnt，将只出现在所有字符串中的字符添加到结果列表res中。

        返回包含公共字符的结果列表。
        """
        cnt, res = {s: [float('inf'), 0] for s in string.ascii_lowercase}, []
        for w in A:
            for k, v in collections.Counter(w).items():
                # 更新字母k的最小出现次数
                cnt[k][0] = min(cnt[k][0], v)
                # 记录字符k在字符串列表A中的出现次数加一
                cnt[k][1] += 1
        for k in cnt:
            if cnt[k][1] == len(A):
                # 将只出现在所有字符串中的字母添加到结果中，数量为最小频次
                res += [k] * cnt[k][0]
        return res
