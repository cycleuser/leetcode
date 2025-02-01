
class Solution:
    # 判断给定的手牌是否能组成W张连续的牌
    def isNStraightHand(self, hand: list[int], W: int) -> bool:
        # 对手牌进行排序，便于后续判断连续性
        hand.sort()

        while hand:
            try:
                # 以第一个元素作为基数，尝试移除接下来W-1张连续的牌
                base = hand[0]
                for i in range(W):
                    hand.remove(base + i)
            except:
                return False

        return True
