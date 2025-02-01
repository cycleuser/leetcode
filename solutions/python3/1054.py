
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        使用计数器统计每个条形码的出现次数，按降序排列。
        
        :param barcodes: 列表形式的条形码数字
        :return: 重新安排后的条形码列表
        
        中文注释：
        - 使用 collections.Counter 统计条形码出现频率，并按降序排序。
        - 将频率较高的条形码先加入到临时列表 ref 中，方便后续间隔放置。
        - 遍历原列表，偶数位置填入高频条形码，奇数位置填入剩余的低频条形码。
        """
        
        from collections import Counter
        cnt = Counter(barcodes).most_common()[::-1]
        ref = [val for val, t in cnt for _ in range(t)]
        
        # 交替放置高频率和低频率的条形码到原列表中
        for i in range(0, len(barcodes), 2):
            barcodes[i] = ref.pop()
        for i in range(1, len(barcodes), 2):
            barcodes[i] = ref.pop()

        return barcodes
