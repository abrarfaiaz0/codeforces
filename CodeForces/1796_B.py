t = int(input())
for q in range(t):
    found = False
    index = 0
    a = input()
    b = input()
    if(a[0] == b[0]):
        print("YES")
        print(f"{a[0]}*")
        continue
    elif(a[len(a)-1] ==b[len(b)-1]):
        print("YES")
        print(f"*{a[len(a)-1]}")
        continue
    for i in range(len(a)):
        if found == True:
            break
        for j in range(len(b)):
            if(a[i] == b[j]):
                if(a[i:i+2] == b[j:j+2]):
                    found = True
                    index = i
                    break
    if found == False:
        print("NO")
    else:
        print("YES")
        print(f"*{a[index:index+2]}*")
    
    
                     
            



     
