class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        dic = {}
        for elem in words:
           s = "".join(sorted(elem))
           if  dic.get(s,0) != 0:
                dic[s] += [elem]
           else:
                dic[s] = [elem]
        
        return [val for val in dic.values()]
            
                   

if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()