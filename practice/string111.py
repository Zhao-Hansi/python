s = "abcd"
if len(s) % 2 == 0:
    mid = ""
else:
    index = int(len(s) % 2 + len(s)//2)
    mid = s[index - 1]
print(mid)