
class WordFilter:
    # 初始化字典树结构，用于存储前缀和后缀信息
    def __init__(self, words):
        from collections import defaultdict
        self.prefixes, self.suffixes, self.index_map = defaultdict(set), defaultdict(set), {}
        
        for i, w in enumerate(words): 
            # 记录每个单词的索引
            self.index_map[w] = i
            
            # 初始化根节点，添加当前词作为前缀和后缀
            self.prefixes[""].add(w)
            self.suffixes[""].add(w)
            
            # 遍历每个可能的前缀并记录在字典中
            for i in range(1, len(w) + 1): 
                self.prefixes[w[:i]].add(w)
                
                # 记录每个可能的后缀
                self.suffixes[w[-i:]].add(w)

    # 根据前缀和后缀查找最匹配的单词索引
    def f(self, prefix, suffix):
        return max((self.index_map[c] for c in self.prefixes[prefix] & self.suffixes[suffix]), default = -1)



class WordFilter:
    # 初始化字典树结构，用于存储前缀和后缀信息
    def __init__(self, words):
        from collections import defaultdict
        self.prefixes, self.suffixes, self.index_map = defaultdict(set), defaultdict(set), {}
        
        for i, w in enumerate(words): 
            # 记录每个单词的索引
            self.index_map[w] = i
            
            # 初始化根节点，添加当前词作为前缀和后缀
            self.prefixes[""].add(w)
            self.suffixes[""].add(w)
            
            # 遍历每个可能的前缀并记录在字典中
            for i in range(1, len(w) + 1): 
                self.prefixes[w[:i]].add(w)
                
                # 记录每个可能的后缀
                self.suffixes[w[-i:]].add(w)

    # 根据前缀和后缀查找最匹配的单词索引
    def f(self, prefix, suffix):
        return max((self.index_map[c] for c in self.prefixes[prefix] & self.suffixes[suffix]), default = -1)
