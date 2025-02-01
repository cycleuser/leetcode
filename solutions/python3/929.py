
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        计算去重后的有效唯一邮箱数量

        :param emails: 邮箱列表
        :return: 唯一有效邮箱的数量
        """
        rec = set()  # 使用集合来存储唯一的有效邮箱地址
        
        for email in emails:
            local, domain = email.split('@')  # 分割本地部分和域名部分
            local = local.split('+')[0].replace('.', '')  # 移除'+'及其后的所有内容，并替换"."为空字符
            
            # 构造处理后的有效邮箱地址并添加到集合中，利用set的唯一性自动去重
            rec.add(local + '@' + domain)
        
        return len(rec)  # 返回去重后邮箱的数量
