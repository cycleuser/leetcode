
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 使用集合存储所有文件夹，以提高查找效率
        # Chinese: 使用集合来存储所有的文件夹，以提高查找的效率
        
        st = set(folder)
        
        for f in folder:
            # 遍历每个文件夹，并检查其子路径是否也在集合中
            # Chinese: 遍历每个文件夹，并检查其子路径是否也在集合中
            if any(p in st for p in itertools.accumulate(f.split('/'), lambda x, y: x + '/' + y) if p and p != f):
                st.discard(f)
        
        # 返回最终的不包含子路径的文件夹列表
        return list(st)
