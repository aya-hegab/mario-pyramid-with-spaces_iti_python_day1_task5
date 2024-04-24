# num = 4
userNum = input("enter number ")
while not userNum.isdigit():
  userNum = input("enter number ")

num = int(userNum)
for i in range(num + 1):
  print(" " * (num - i), end="")
  for j in range(i):
    print("*", end="")
  print("")

