# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        * 递归

        时间复杂度 height,利用h1找到删除节点，利用h2调整删除之后的节点，(h1+h2)=height
        空间复杂度 height

        注意：二叉搜索树，保持左>中>右

        """

        def pre_node(root):
            # 找到左子树里最大的(right)作为root
            dummy = root.left
            while dummy.right:
                dummy = dummy.right
            return dummy.val

        def post_node(root):
            # 找到右子树里最小(left)的作为root
            dummy = root.right
            while dummy.left:
                dummy = dummy.left
            return dummy.val

        def delete(root, key):
            if not root:
                return None
            if root.val > key:
                root.left = delete(root.left, key)
            elif root.val < key:
                root.right = delete(root.right, key)
            else:
                # 叶子结点的话，直接none
                if not root.left and not root.right:
                    root = None
                # 有右子树，就找到右子树里最小的作为root，再调整右子树
                elif root.right:
                    root.val = post_node(root)  # 则用它的后继节点的值替代
                    root.right = delete(root.right, root.val)  # 删除后继节点
                # 只有左子树，就找到左子树里最大的作为root，再调整左子树
                else:
                    root.val = pre_node(root)
                    root.left = delete(root.left, root.val)
            return root

        return delete(root, key)
