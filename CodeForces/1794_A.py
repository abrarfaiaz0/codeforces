t = int(input())
pattern = "FBFFBFFBFBFFBFFBFB"
for q in range(t):
    n = int(input())
    ls =  input()
    ls = ls.split()
    flag = 0
    for s1 in ls:
        for s2 in ls:
            if len(s1)==len(s2) and ls.index(s1)!=ls.index(s2)):
                if(s1!=s2[::-1]):
                    flag = 1
    if (flag==0):
        print("YES")
    else: print("NO")
    
