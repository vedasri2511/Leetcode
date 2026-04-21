class Solution:
    def sumOfLeftLeaves(self, root):
        res, st = 0, [(root, False)]
        while st:
            n, l = st.pop()
            if not n: continue
            if not n.left and not n.right and l:
                res += n.val
            st += [(n.left, True), (n.right, False)]
        return res