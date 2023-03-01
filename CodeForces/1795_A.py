t = int(input())
for q in range(t):
    inp = input()
    a = input()
    b = input()
    s = a+b[::-1]
    mtch = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            mtch+=1
    if(mtch>1):
        print("NO")
    else:
        print("YES")

