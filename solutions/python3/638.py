
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # 定义深度优先搜索函数，参数为当前已选物品总价和剩余需求
        def dfs(cur: int, needs: List[int]) -> int:
            # 计算不使用任何优惠券的直接购买成本
            val = cur + sum(p * needs[i] for i, p in enumerate(price))
            # 遍历所有优惠券组合
            for s in special:
                # 检查当前需求是否满足使用该优惠券的条件，即每种商品数量都不小于优惠券中要求的数量
                if all(n >= s[i] for i, n in enumerate(needs)):
                    # 更新最小总成本为当前值与使用优惠券后的新组合价格中的较小者
                    val = min(val, dfs(cur + s[-1], [n - s[i] for i, n in enumerate(needs)]))
            return val

        # 从0元开始，根据初始需求调用dfs函数计算最小花费
        return dfs(0, needs)
