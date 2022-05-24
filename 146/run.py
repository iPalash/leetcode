class Node:
    def __init__(self,k=None, val=None, prv=None, nxt=None) -> None:
        self.k=k
        self.val = val
        self.prv = prv
        self.nxt = nxt

    def __repr__(self):
        return str(self.k)+":"+str(self.val)

class LRUCache:
    def __init__(self, capacity):
        self.keys = {}
        self.capacity = capacity
        self.count = 0
        first = Node(-1,-1)
        last = Node(-1,-1)
        first.nxt = last
        last.prv = first
        self.first =  first
        self.last = last 

    def _printList(self):
        c = self.first.nxt
        a=""
        while c.val!=-1:
            a+="{}:{} ".format(c.k,c.val)
            c=c.nxt
        print(a)
        

    def _delete(self, k) -> int:
        node = self.keys.get(k,None)
        if node:
            prv=node.prv
            nxt=node.nxt
            prv.nxt=nxt
            nxt.prv=prv
            del self.keys[k]
            return node.val
        return -1
    def _insert(self,k,v):
        node = Node(k,v,self.last)
        self.last.prv.nxt,node.prv,node.nxt,self.last.prv=node,self.last.prv,self.last,node

        self.keys[k]=node

    def get(self, key) -> int:
        if key in self.keys:
            val=self._delete(key)
            self._insert(key,val)
            return val
        else:
            return -1

    def put(self, key, value) -> None:
        if key in self.keys:
            self._delete(key)
            self._insert(key,value)
        elif self.count<self.capacity:
            self._insert(key,value)
            self.count+=1
        else:
            self._delete(self.first.nxt.k)
            self._insert(key,value)

ops = input()[2:-2].split('","')
args = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(ops,args)
t = None
for op,arg in zip(ops,args):
    if op=='LRUCache':
        t = LRUCache(arg[0])
    else:
        method = getattr(t, op)
        print("calling {} with args {}".format(op,arg))
        if op=='put':
            r = method(key=arg[0],value=arg[1])
        else:
            r = method(key=arg[0])
        t._printList()


