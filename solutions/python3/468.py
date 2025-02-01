
class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str

        判断给定的字符串IP是否为有效的IPv4或IPv6地址。
        1. 首先检查是否符合IPv4格式，即由四个部分组成，每个部分由点分隔。
        2. 检查每个部分是否满足IPv4规则：长度在0到3之间，数字0-9开头且不超过255。同时，以'0'开头但不等于"0"的情况视为无效。
        3. 如果符合IPv4格式，则返回 "IPv4"。

        4. 检查是否符合IPv6格式，即由八个部分组成，每个部分由冒号分隔。
        5. 每个部分应为1-4位的十六进制数字。
        6. 如果符合IPv6格式，则返回 "IPv6"。

        如果不符合上述任何规则，则返回 "Neither"。
        """
        ip4, ip6 = IP.split("."), IP.split(":")
        
        # IPv4 validation
        if len(ip4) == 4:
            for num in ip4:
                try: 
                    if not (num[0] in string.digits and int(num) < 256 and (num[0] != "0" or num == "0")): return "Neither"
                except: 
                    return "Neither"
            return "IPv4"

        # IPv6 validation
        elif len(ip6) == 8:
            for num in ip6:
                try: 
                    if not (num[0] in string.hexdigits and 0 <= int(num, 16) < 65536 and len(num) <= 4): return "Neither"
                except: 
                    return "Neither"
            return "IPv6"

        return "Neither"
