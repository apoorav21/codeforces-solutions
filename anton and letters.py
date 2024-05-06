s = input()
x = set(s)
try:
    x.remove("{")
    x.remove("}")
    x.remove(" ")
    x.remove(",")
except:
    pass
print(len(x))