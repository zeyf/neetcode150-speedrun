class Solution:

    def dfs(self, u, graph, visited):
        visited.add(u)

        for v in graph[u]:
            if v not in visited:
                self.dfs(v, graph, visited)


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for u, v in edges:
            if u not in graph:
                graph[u] = [v]
            else:
                graph[u].append(v)

            if v not in graph:
                graph[v] = [u]
            else:
                graph[v].append(u)
        
        visited = set()

        components = 0
        for node in range(n):
            if node not in graph:
                components += 1
            elif node not in visited:
                components += 1
                self.dfs(node, graph, visited)
        
        return components
