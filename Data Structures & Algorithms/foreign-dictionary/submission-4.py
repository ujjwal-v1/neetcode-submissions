class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}
        n = len(words)
        for i in range(n-1):
            a, b = words[i], words[i+1]
            la, lb = len(a), len(b)
            j = 0
            while j<la and j<lb:
                if a[j]!=b[j]:
                    adjList[a[j]].add(b[j])
                    break
                j+=1
            if la != lb and j>=lb:
                return ""

        ans = ""
        vis = {}

        def dfs(node):
            nonlocal ans
            if node in vis:
                return vis[node]==2
            vis[node]=1
            for n2 in adjList[node]:
                if not dfs(n2):
                    return False
            vis[node]=2
            ans+=node
            return True
        
        for node in adjList:
            if node not in vis:
                if not dfs(node):
                    return ""

        return ans[::-1]
