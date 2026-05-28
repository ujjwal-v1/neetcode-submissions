class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adjList = {c: set() for word in words for c in word}
        invalid = False

        for i in range(1, n):
            a, b, len1, len2 = words[i-1], words[i], len(words[i-1]), len(words[i])
            j = 0
            while j<len1 and j<len2:
                if a[j]==b[j]:
                    j+=1
                    continue
                else:
                    adjList[a[j]].add(b[j])
                    break
            
            if len1 != len2 and j>=len2:
                return ""
        
        ans = ""
        cycle = False
        vis = {}

        def dfs(node):
            nonlocal ans, cycle
            vis[node] = 1
            for n2 in adjList[node]:
                if n2 not in vis:
                    dfs(n2)
                elif vis[n2]==1:
                    cycle = True
                elif vis[n2]==0:
                    continue
            vis[node]=0
            ans+=node

        for char in adjList:
            if char not in vis:
                dfs(char)
        
        for char in adjList:
            if char not in ans:
                ans+=char

        return "".join(reversed(ans)) if not cycle else ""