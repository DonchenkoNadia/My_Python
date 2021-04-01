class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        ans = []
        print(l)
        for i in l:
            if len(set(i)) == 1:
                ans.append(i[0])
            else:
                break
        return "".join(ans)
