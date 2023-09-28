# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# function to delete the repeated letters

def cleanWord(word):

  if (len(word) == 1):
    return word

  if (word[0] == word[1]):

    print(f"Print Before Condition: {word}") # for trace

    return cleanWord(word[1:])

  print(f"Print Before Return: {word}") # for trace

  return word[0] + cleanWord(word[1:])


print(cleanWord("WWWoooorrrldd"))