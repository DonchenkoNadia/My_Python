telephone = { "2" : ["a", "b", "c"],
              "3" : ["d", "e", "f"],
              "4" : ["g", "h", "i"],
              "5" : ["j", "k", "l"],
              "6" : ["m", "n", "o"],
              "7" : ["p", "q", "r", "s"],
              "8" : ["t", "u", "v"],
              "9" : ["w", "x", "y", "z"]
}
digits = "23"
combinations = []

def backtrack(index, path):
    # If the path is the same length as digits, we have a complete combination
    if len(path) == len(digits):
        combinations.append("".join(path))
        return # Backtrack

    # Get the letters that the current digit maps to, and loop through them
    possible_letters = telephone.get(digits[index], [])
    for letter in possible_letters:
        # Add the letter to our current path
        path.append(letter)
        # Move on to the next digit
        backtrack(index + 1, path)
        # Backtrack by removing the letter before moving onto the next
        path.pop()

backtrack(0, [])

print(combinations)
