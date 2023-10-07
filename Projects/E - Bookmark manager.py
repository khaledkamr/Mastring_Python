# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

myBookmark = []
maxWebs = 5 

while (maxWebs > 0):
  web = input("Website Name Without 'https://' ")
  myBookmark.append(f"https://{web.strip()}")
  
  maxWebs -= 1
  print(f"Website Added, {maxWebs} Places Left")
  print(myBookmark)

else:
  print("Bookmark Is Full, You Cant Add More")

if (len(myBookmark) > 0):
  myBookmark.sort()
  index = 0

  print("Printing The List Of Websites in Your Bookmark")

  while (index < len(myBookmark)):
    print(myBookmark[index])
    index += 1  