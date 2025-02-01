
class Solution:
    # 定义一个类来解决问题

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # 使用计数器统计被信任的人的次数，取出现次数最多的那个
        j, cnt = collections.Counter(b for a, b in trust).most_common(1)[0] if trust else (N, 0)
        
        # 如果这个人没有信任任何人，并且被其他 N-1 个人信任，则他是法官
        return j if j not in {a for a, b in trust} and cnt == N - 1 else -1
        # 返回结果，如果找不到法官则返回 -1
