
class Solution:
    # 定义一个方法来模拟逐步揭示升序排列的牌
    def deckRevealedIncreasing(self, deck):
        # 创建指示器列表，记录当前待揭示的牌的位置
        ind = list(range(len(deck)))
        
        # 对输入的deck进行排序
        for num in sorted(deck):
            # 将当前数字放置在指示器列表的第一个位置
            deck[ind[0]] = num
            
            # 更新指示器列表：移除第一个元素，并将第二个元素移动到末尾
            if len(ind) > 1:
                ind = ind[2:] + [ind[1]]
        
        return deck
