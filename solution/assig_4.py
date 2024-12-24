s = "this is a string."
rev = ""
index = len(s) - 1
while index >= 0:
    rev += s[index]
    index -= 1
print(rev)
