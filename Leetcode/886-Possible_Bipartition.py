"""
https://leetcode.com/problems/possible-bipartition/

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false



Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""


class Solution:
    def dfs(self, i, group):
        if i in self.group_mapping and group != self.group_mapping[i]:   # Check if there is a conflict
            return False                                                 # between given group and existing group
        self.group_mapping[i] = group
        if i not in self.visited:
            self.visited.add(i)
            for dis in self.graph[i]:                                    # DFS for each dislike node recursively
                if not self.dfs(dis, not group): return False            # Assign contrary group to dislike node
        return True    
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        self.visited, self.group_mapping = set(), {}
        for (u, v) in dislikes:                                          # Create graph 
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, N+1):                                          # DFS until eror
            if i not in self.visited:                                    # We don't want to revisit since it's DFS
                if not self.dfs(i, True):                                # If conflict occurs during DFS, return False
                    return False
        return True


    def possibleBipartitionBFS(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        group_mapping = {}
        for (u, v) in dislikes:                             # Create graph
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        visited = set()
        for i in range(1, N + 1):                           # Iterate each node
            if i in visited: continue                       # No need to revisit, since it's a non-directed graph
            stack = [(i, 0)]                                # Use stack for BFS
            while stack:                                    # You can also use a deque instead of 2 while loop on stack
                tmp_stack = []
                while stack:                                # exhaust current stack before go to next layer (BFS)
                    cur_node, group = stack.pop()
                    if cur_node in group_mapping and group != group_mapping[cur_node]:  # check if it's conflict
                        return False
                    if cur_node in visited: continue        # If visited and no conflict, continue to avoid dead loop
                    group_mapping[cur_node] = group         # Assign group for current node
                    visited.add(cur_node)
                    for child in self.graph[cur_node]:      # Assign contrary group for dislikes of current node
                        tmp_stack.append((child, not group))
                stack = tmp_stack            
        return True   