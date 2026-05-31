class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}
        n = len(words)

        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            l1, l2 = len(w1), len(w2)
            j = 0

            while j<l1 and j<l2:
                if w1[j]!=w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
                j+=1
            
            if l1!=l2 and j>=l2:
                return ""
        
        ans = []
        vis = {}

        def dfs(node):
            if node in vis:
                return vis[node]==1

            vis[node]=0
            for n2 in adjList[node]:
                if not dfs(n2):
                    return False

            vis[node]=1
            ans.append(node)
            return True

        for node in adjList:
            if node not in vis:
                if not dfs(node):
                    return ""
        
        return "".join(reversed(ans))
        