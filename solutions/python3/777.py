
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        判断是否可以通过平移'L'和'R'字符来使start变为end。
        
        通过字典记录L和R在start和end中的位置，然后进行比较验证。
        """

        # 使用defaultdict存储L和R的位置
        s, e = collections.defaultdict(list), collections.defaultdict(list)
        
        # 将不含空格的字符分别存入s和e中
        newS, newE = [c for c in start if c != "X"], [c for c in end if c != "X"]
        
        # 记录L和R在start中的位置
        for i in range(len(start)):
            if start[i] != "X":
                s[start[i]].append(i)
                
        # 记录L和R在end中的位置
        for i in range(len(end)):
            if end[i] != "X":
                e[end[i]].append(i)
        
        # 检查字符数量是否一致，以及L和R的位置关系
        if newS == newE and len(s["L"]) == len(e["L"]) and len(s["R"]) == len(e["R"]):
            # L只能向左移动，R只能向右移动，验证位置合法性
            if all(s["R"][i] <= e["R"][i] for i in range(len(s["R"]))) and all(s["L"][i] >= e["L"][i] for i in range(len(s["L"]))):
                return True
        
        return False
