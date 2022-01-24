class Solution:
    def shortestWay(self, source, target):
        # sounds like it is a number of traversal of source string in order to build a target
        # the idea is two pointers
        # the first pointer have to be put on the beginning of target
        # the second may be on the beginning of source
        # in case first pointer in target string is pointing on some character
        # which can't be found in source - we can return -1

        found = 1
        iterations = 0
        t = 0

        while t < len(target):

            if found == 0:
                return -1

            found = 0
            s = 0

            while s < len(source) and t < len(target):
                if target[t] == source[s]:
                    t += 1
                    s += 1
                    found = 1
                else:
                    s += 1

            iterations += 1

        return iterations

obj = Solution()
print(obj.shortestWay("aaaaa", "aaaaaaaaaaaaa"))
