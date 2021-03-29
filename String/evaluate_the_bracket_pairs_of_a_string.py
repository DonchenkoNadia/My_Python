class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        #all the ideas taken from @DBabichev
        #first good idea is to create a dict instead of lists
        d = {k:v for k, v in knowledge}

        #then use split approach
        lst = s.split("(")
        result = lst[0]

        for i in range(1, len(lst)):

            #cool, that in python you are allowed to put result in two variables
            question, word = lst[i].split(")")
            result += d.get(question, "?") + word

        return result
