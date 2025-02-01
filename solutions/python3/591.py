
class Solution:
    # CDATA区开始和结束标记
    CDATA_BEGIN = '![CDATA['
    CDATA_END = ']]>'

    def isValid(self, S: str) -> bool:
        """
        判断给定的字符串S是否为有效的HTML标签格式。
        - CDATA_BEGIN 和 CDATA_END 用于标记CDATA区段

        :param S: 输入的字符串
        :return: 如果输入满足HTML标签格式返回True，否则返回False
        """

        def collect_tag(i: int) -> str:
            """
            收集从索引i开始的标签内容。
            - 遇到 '>' 结束
            - 若未遇到 '>', 返回None

            :param i: 开始收集标签的位置
            :return: 标签内容或None
            """

            for j in range(i, len(S)):
                if S[j] == '>': break
            else:
                return None
            return S[i+1:j]

        def valid_tag(tag: str) -> bool:
            """
            判断给定的tag是否有效。
            - tag长度在1到9之间且仅包含大写字母

            :param tag: 要验证的标签字符串
            :return: 如果有效返回True，否则False
            """

            return 1 <= len(tag) <= 9 and all('A' <= c <= 'Z' for c in tag)

        # 检查输入格式
        if not S or S[0] != '<': 
            return False

        # 获取初始标签
        tag = collect_tag(0)
        if (tag is None or 
                not S.startswith('<{}>'.format(tag)) or 
                not S.endswith('</{}>'.format(tag)) or
                not valid_tag(tag)):
            return False
        
        # 去除已验证的起始和结束标签
        S = S[len(tag) + 2: -len(tag) - 3]

        i = 0
        stack = []
        
        while i < len(S):
            if S[i] == '<':
                tag = collect_tag(i)
                if tag is None: return False
                
                # 检查CDATA区段
                if tag.startswith(CDATA_BEGIN):
                    while i < len(S) and S[i:i+3] != CDATA_END:
                        i += 1
                    if not S[i:i+3] == CDATA_END:
                        return False
                    i += 2
                
                # 检查结束标签
                elif tag.startswith('/'):
                    tag = tag[1:]
                    if not valid_tag(tag) or not stack or stack.pop() != tag:
                        return False
                    
                # 添加新的开始标签到栈中
                else:
                    if not valid_tag(tag):
                        return False
                    stack.append(tag)
            i += 1

        # 栈为空表示所有标签都正确闭合
        return not stack
