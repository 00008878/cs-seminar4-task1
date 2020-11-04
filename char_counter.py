word = input("word:")
chara = input("letter:")
count = 0
for letter in word:
  if letter == chara:
    count += 1
print(count)
