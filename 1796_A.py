t = input()
pattern = "FBFFBFFBFBFFBFFBFB"
for j in range(0,int(t)):
    n = int(input())
    s = input()
    if s in pattern:
        if (s==""):
            print("NO")
            continue
        print("YES")
    else: 
        print("NO")


