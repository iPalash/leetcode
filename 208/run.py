
class TrieNode:
    def __init__(self) -> None:
        self.val = ''
        self.children = [None]*27

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            idx = ord(letter)-97
            if curr.children[idx]==None:
                # Make a node and insert it here
                curr.children[idx]=TrieNode()
            curr=curr.children[idx]
        curr.children[26]='$'

    def search(self, word):
        curr = self.root
        for letter in word:
            idx = ord(letter)-97
            if curr.children[idx]==None:
                return False
            curr=curr.children[idx]
        return curr.children[26]=='$'
                

    def startsWith(self, prefix):
        curr = self.root
        for letter in prefix:
            idx = ord(letter)-97
            if curr.children[idx]==None:
                return False
            curr=curr.children[idx]
        return True





ops = input()[2:-2].split('","')
args = [el[1:-1] for el in input()[2:-2].split("],[")]

print(ops,args)
t = None
for op,arg in zip(ops,args):
    if op=='Trie':
        t = Trie()
    else:
        method = getattr(t, op)
        print("calling {} with args {}".format(op,arg),method(arg))
