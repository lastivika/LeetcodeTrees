# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        postfix = self._postorder(root)

        stack = []
        for el in postfix:
            if el == 2:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 or val2)
            elif el == 3:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 and val2)
            else:
                stack.append(el)
        return stack[0]

    @classmethod
    def _postorder(cls, root):
        if root.val < 2:
            return [bool(root.val)]
        return cls._postorder(root.left) + cls._postorder(root.right) + [root.val]


        