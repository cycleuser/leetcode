
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 初始化计数器s和g，分别用于记录秘密中未匹配的数字及其在猜测中的数量、猜测中未匹配的数字及其在秘密中的数量
        s, g = collections.defaultdict(int), collections.defaultdict(int)
        a, b = 0, 0  # a表示正确位置的数量，b表示正确数字但位置错误的数量

        for i in range(len(secret)):
            # 如果当前位置上的数字匹配，则a加1
            if secret[i] == guess[i]:
                a += 1
                continue
            
            # 如果猜测中的数字在秘密中已出现过，则增加b计数，减少s中相应计数，并将猜测中的该数字加入g记录
            if s[guess[i]] > 0:
                b, s[guess[i]] = b + 1, s[guess[i]] - 1
                g[guess[i]] += 1

            # 如果秘密中的数字在猜测中已出现过，则增加b计数，减少g中相应计数，并将秘密中的该数字加入s记录
            if g[secret[i]] > 0:
                b, g[secret[i]] = b + 1, g[secret[i]] - 1
                s[secret[i]] += 1
        
        # 返回结果格式化字符串，包含正确位置和正确数字但位置错误的数量
        return "%dA%dB" % (a, b)
