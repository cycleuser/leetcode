
class Solution:
    # 定义一个类来处理PII掩码

    def maskPII(self, S: str) -> str:
        # 如果输入字符串包含@
        if "@" in S:
            # 将字符串转换为小写并按@分割
            s = S.lower().split("@")
            # 返回格式化后的电子邮件地址
            return s[0][0] + "*" * 5 + s[0][-1] + "@" + s[1]
        else:
            # 定义一个集合来存储数字字符
            nums, tmp = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}, ""
            # 遍历字符串中的每个字符
            for c in S:
                if c in nums:  # 如果是数字，添加到临时变量中
                    tmp += c
            # 根据电话号码长度返回不同格式的掩码
            return "+" + "*" * (len(tmp) - 10) + "-***-***-" + tmp[-4:] if len(tmp) > 10 else "***-***-" + tmp[-4:]
