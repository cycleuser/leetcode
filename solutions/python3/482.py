
class Solution:
    # 定义一个类来处理许可证格式化

    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # 移除字符串中的 '-'，转换为大写，并反转字符串
        S = S.replace("-", "").upper()[::-1]
        
        # 使用切片将字符串分割成长度为K的子串，并用 '-' 连接这些子串，最后再反转回来
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]
