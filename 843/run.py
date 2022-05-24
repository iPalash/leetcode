class Master:
    def __init__(self, secret):
        self.secret=secret
    def guess(self, word):
        print(word)
        i=0
        for j in range(6):
            i+=int(self.secret[j]==word[j])
        return i

class Solution:
    def findSecretWord(self, wordlist: list[str], master: 'Master') -> None:

        wordlist.sort()

        
        avoid = set()

        def updateAvoid(n,guess):
            for word in wordlist:
                cnt=0
                if word not in avoid:
                    for i in range(6):
                        cnt+=int(word[i]==guess[i])
                if cnt!=n:
                    avoid.add(word)


        i=0
        while i<len(wordlist):
            if wordlist[i] not in avoid:
                match = master.guess(wordlist[i])
                if match==6:
                    break
                updateAvoid(match,wordlist[i])
            i+=1



secret = input()[1:-1]

wordlist = [el for el in input()[2:-2].split('","')]


print(Solution().findSecretWord(wordlist,Master(secret)))




