class Solution:
    def generateParenthesis(self, n: int) :
        res = []

        def DFS(paths, l, r):
            if l > n or r > l:
                return
            if len(paths) == n*2:
                res.append(paths)
                return

            DFS(paths + '(', l+1, r)
            DFS(paths + ')', l, r+1)

        DFS('', 0, 0)
        return res

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))