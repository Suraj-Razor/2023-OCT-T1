# take a, b and cas input from the user
a = int(input("Enter first nunber"))
b = int(input("Enter second nunber"))
c = int(input("Enter third nunber"))

#if a > b
if a > b:
  # if a > c
  if a > c:
    # display a
    print(a)
  #else
  else:
    #display c
    print(c)
#else
else:
  #if b > c
  if b > c:
    # display b
    print(b)
  #else
  else:
    # display c
    print(c)