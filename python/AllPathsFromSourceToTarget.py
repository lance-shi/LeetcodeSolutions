# Question No. 797
# All Paths From Source to Target
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(cur, node):
            cur_cp = cur.copy()
            cur_cp.append(node)
            if node == n - 1:
                ans.append(cur_cp)
                return
            else:
                for nd in graph[node]:
                    dfs(cur_cp, nd)
        dfs([], 0)
        return ans
