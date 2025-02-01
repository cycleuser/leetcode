
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # 中文注释：当 sx 小于 tx 且 sy 小于 ty 时，通过取模操作逐步缩小 tx 和 ty 的值。
        # English comment: When sx is less than tx and sy is less than ty, reduce tx and ty by using modulo operation.
        
        while sx < tx and sy < ty:
            # 中文注释：通过取余操作更新 tx 和 ty，确保 tx 保持大于等于 sx 且 ty 保持大于等于 sy。
            # English comment: Update tx and ty with modulo operations to ensure tx >= sx and ty >= sy.
            
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        # 中文注释：检查最终的 tx 和 ty 是否满足条件，即 tx 是否等于 sx 且 (ty - sy) 能被 sx 整除，或者 ty 等于 sy 且 (tx - sx) 能被 sy 整除。
        # English comment: Check if the final tx and ty satisfy the conditions, i.e., tx equals sx and (ty - sy) is divisible by sx, or ty equals sy and (tx - sx) is divisible by sy.
        
        return sx == tx and (ty - sy) % sx == 0 or sy == ty and (tx - sx) % sy == 0
