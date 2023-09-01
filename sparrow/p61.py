#pallindrome or not
str=input("enter string")
revstr="".join(reversed(str))
print(revstr)
if str==revstr:
    print("string is pallindrome")
else:
    print("not pallindrome")
