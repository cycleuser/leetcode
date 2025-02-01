
class Solution:
    def evaluate(self, expression):
        # 初始化作用域和表达式项列表，根节点默认为"root"
        scopes, items = [{}], [["root"]]
        
        for item in expression.replace(")", " )").split():
            if item[0] == "(":
                # 遇到新的表达式块，添加新项并判断当前操作类型
                items.append([item[1:]])
                if item[1:] == "let":
                    scopes.append(dict(scopes[-1]))
                continue
            
            elif item == ")": 
                # 结束一个表达式块，根据块的类型进行计算或返回结果，并更新作用域和项列表
                if items[-1][0] == "add":
                    item = str(int(items[-1][1]) + int(items[-1][-1]))
                elif items[-1][0] == "mult":
                    item = str(int(items[-1][1]) * int(items[-1][-1]))
                else:
                    item = items[-1][-1]
                    if item in scopes[-1]:
                        item = scopes[-1][item]
                    scopes.pop()
                items.pop()
            
            # 判断当前项是否已在作用域中，并根据情况进行值替换或更新
            if item in scopes[-1] and (items[-1][0] != "let" or len(items[-1]) % 2 == 0):
                item = scopes[-1][item]
            
            # 处理"let"表达式，记录变量名和对应值
            if items[-1][0] == "let" and item.lstrip("-").isdigit():
                scopes[-1][items[-1][-1]] = item
            
            # 将当前项添加到当前操作的末尾
            items[-1].append(item)
        
        # 返回最终结果
        return int(items[-1][-1])
