
class Solution:
    # 判断一个数字是否是回文旋转变换数（strobogrammatic number）
    
    def isStrobogrammatic(self, num: str) -> bool:
        # 检查每个可能的配对字符是否符合回文旋转变换的要求
        return not any(num[i] + num[-1-i] not in ("88", "69", "96", "11", "00") for i in range((len(num) + 1) // 2))
