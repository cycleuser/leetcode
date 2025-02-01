
class Solution:
    # 使用lambda表达式定义交集方法，输入三个可迭代对象，返回它们的交集列表
    intersect = lambda self, nums1, nums2, nums3: [k for k, v in (collections.Counter(nums1) & collections.Counter(nums2)).items() for _ in range(v)] \
                                                   + [k for k, v in (collections.Counter(nums2) & collections.Counter(nums3)).items() for _ in range(v)] \
                                                   + [k for k, v in (collections.Counter(nums1) & collections.Counter(nums3)).items() for _ in range(v)]
