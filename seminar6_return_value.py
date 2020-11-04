x = input("x:")
y = input("y:")
def check():
  if x > y:
    return 1
  elif x == y:
    return 0
  else:
    return -1

print(check())
