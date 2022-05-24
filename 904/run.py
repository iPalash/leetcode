from collections import deque
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        i=0
        n=len(fruits)
        j=1
        d=1
        unique = {}
        q = deque()
        count = 0
        start = 0
        end = 0
        mx = 1
        while end<len(fruits):
            curr=fruits[end]
            if curr not in unique and count<2:
                # insert into unique
                unique[curr]=1
                count+=1
                q.append([curr,end])
                mx=max(mx,end-start+1)
            elif curr not in unique and count==2:
                unique[curr]=1
                # pop from queue
                [el,idx]=q.popleft()
                q.append([curr,end])
                start=idx+1
                del unique[el]
            elif curr in unique:
                # update queue
                if q[0][0]==curr:
                    q.popleft()
                    q.append([curr,end])
                else: # update rightmost
                    q[-1]=[curr,end]
                mx=max(mx,end-start+1)
            end+=1
        return mx

fruits = [int(el) for el in input()[1:-1].split(',')]
print(Solution().totalFruit(fruits))
            
            
            
            
        
        
        
        
