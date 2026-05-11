class Solution:
    def findMode(self, root):
        prev = None
        cnt = mx = 0
        ans = []

        def inorder(node):
            nonlocal prev, cnt, mx, ans
            if not node:
                return
            
            inorder(node.left)

            if prev == node.val:
                cnt += 1
            else:
                cnt = 1

            if cnt > mx:
                mx = cnt
                ans = [node.val]
            elif cnt == mx:
                ans.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return ans