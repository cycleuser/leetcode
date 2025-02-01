
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        # 返回某年某月的天数，中文注释：计算给定年份和月份的总天数
        return 29 + {2: 
            # 如果是2月且不是闰年，则返回28天，英文注释：If it's February and not a leap year, return 28 days
            Y % (Y % 25 and 4 or 16) and -1 
        }.get(M, 
            # 根据月份判断是否为偶数月且不在7月之前，返回30或31天，英文注释：If the month is an even number but not before July, return 30 days; otherwise, return 31 days
            ((M % 2) ^ (M > 7)) + 1)
