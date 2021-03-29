class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        #first replacing letters to whitespaces
        #i do not know any other way instead of using list

        lst = list(word)
        for i, ch in enumerate(lst):
            if ch not in "0123456789":
                lst[i] = " "
        word = "".join(lst)

        #now let's separate the result
        lst = word.split(' ')
        ans = set()
        for i in lst:
            if i != '':
                ans.add(int(i))

        return len(ans)
