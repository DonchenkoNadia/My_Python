mapping = {
            'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'
        }

#Map performs the specified function for each item in the list.
#Example:
#list( map(int, ['1','2']) ) #[1, 2]

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"

def decoding (s):

    return int("".join(list(map((lambda i: mapping[i]), list(s)))))

print(decoding("cdb"))
