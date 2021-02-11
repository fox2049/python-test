with open("test.txt", "a+") as f:
    f.write("i love you")
with open("test.txt", "a+") as f:
    a = f.read()
    print(a)
