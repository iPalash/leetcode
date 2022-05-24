class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill:int) -> list[int]:
        print(pid,ppid, kill)

        class TreeNode:
            def __init__(self,pid):
                self.pid = pid
                self.children = []
                self.parent = None
        processMap = {}
        for process,parent in zip(pid,ppid):
            p = processMap.get(process, TreeNode(process))
            processMap[process]=p
            if parent==0:
                root = p
            else:
                par = processMap.get(parent,TreeNode(parent))
                processMap[parent]=par
                p.parent = par
                par.children.append(p)

        ans = []

        def dfs(node):
            if node:
                ans.append(node.pid)
                for child in node.children:
                    dfs(child)

        dfs(processMap[kill])
            

        


        return ans

pid = [int(el) for el in input()[1:-1].split(',')]
ppid = [int(el) for el in input()[1:-1].split(',')]
kill = int(input())

print(Solution().killProcess(pid,ppid,kill))
