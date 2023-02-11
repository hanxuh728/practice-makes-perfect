# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive Method: O(N)
        #
        # if (t1 == null)
        #     return t2;
        # if (t2 == null)
        #     return t1;
        # t1.val += t2.val;
        # t1.left = mergeTrees(t1.left, t2.left);
        # t1.right = mergeTrees(t1.right, t2.right);
        # return t1;


        # BFS Method: O(N)
        if root1 is None:
            return root2
        bfs_queue = [(root1, root2)]
        while len(bfs_queue) > 0:
            current = bfs_queue[0]
            if current[0] and current[1]:
                current[0].val += current[1].val
                if current[0].left:
                    if current[1].left:
                        bfs_queue.append((current[0].left, current[1].left))
                else:
                    current[0].left = current[1].left
                if current[0].right:
                    if current[1].right:
                        bfs_queue.append((current[0].right, current[1].right))
                else:
                    current[0].right = current[1].right
            bfs_queue.pop(0)

        return root1