
class Solution:
    # 解决类

    def intersect(self, q1, q2):
        """
        传入两个节点q1和q2，返回它们的交集节点。
        :param q1: Node 类型，第一个节点
        :param q2: Node 类型，第二个节点
        :return: Node 类型，交集结果节点
        """

        # 如果q1是叶子节点
        if q1.isLeaf:
            # 返回值为t的逻辑：如果t有值则返回t，否则返回q2
            return q1.val and q1 or q2

        # 如果q2是叶子节点
        elif q2.isLeaf:
            # 返回值为q2的逻辑：如果q2有值则返回q2，否则返回q1
            return q2.val and q2 or q1

        else:
            # 递归计算左上交集
            tLeft = self.intersect(q1.topLeft, q2.topLeft)
            # 递归计算右上交集
            tRight = self.intersect(q1.topRight, q2.topRight)
            # 递归计算左下交集
            bLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
            # 递归计算右下交集
            bRight = self.intersect(q1.bottomRight, q2.bottomRight)

            # 如果所有子节点都是叶子且值相等，合并为一个叶子节点
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and \
                    tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None)  # 合并后的叶子节点
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)  # 非叶子节点

        return node
