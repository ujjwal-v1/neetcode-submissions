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
        
        
        ans = []
        vis = {}

        def dfs(node):
            if node in vis:
                return vis[node] == 2
            vis[node] = 1
            for n2 in adjList[node]:
                if not dfs(n2):
                    return False
            vis[node] = 2
            ans.append(node)
            return True

        for char in adjList:
            if char not in vis:
                if not dfs(char):
                    return ""

        return "".join(reversed(ans))