# Function Recursion 
### To Understand Recursion, You Need First to Understand Recursion 

## function to delete the repeated letters:
```python []
def cleanWord(word):
  if (len(word) == 1):
    return word

  if (word[0] == word[1]):
    print(f"Print Before Condition: {word}") # for trace
    return cleanWord(word[1:])

  print(f"Print Before Return: {word}") # for trace

  return word[0] + cleanWord(word[1:])


print(cleanWord("WWWoooorrrldd"))
```
#### Output
```
Print Before Condition: WWWoooorrrldd
Print Before Condition: WWoooorrrldd
Print Before Return: Woooorrrldd
Print Before Condition: oooorrrldd
Print Before Condition: ooorrrldd
Print Before Condition: oorrrldd
Print Before Return: orrrldd
Print Before Condition: rrrldd
Print Before Condition: rrldd
Print Before Return: rldd
Print Before Return: ldd
Print Before Condition: dd
World
```