t = int(input())
for q in range(t):
    found = False
    l = int(input())
    s = input().lower()
    flag = 0
    index = 0
    if(len(s)==0):
        print("NO")
        continue
    if(s[0]=='m'):
        flag += 1
        for i in range(len(s)-1):
            if s[i+1] != 'm':
                if(s[i+1]=='e'):
                    flag += 1
                    index = i+1
                    break
                else:
                    found = True
                    break
        for i in range(index,len(s)-1):
            if s[i+1] != 'e':
                if(s[i+1]=='o'):
                    flag += 1
                    index = i+1
                    break
                else:
                    found = True
                    break
        for i in range(index,len(s)-1):
            if s[i+1] != 'o':
                if(s[i+1]=='w'):
                    flag += 1
                    index = i+1
                    break
                else:
                    found = True
                    break
        for i in range(index,len(s)-1):
            if s[i+1] != 'w':
                flag += 1
                found = True
                break
        if found == False and flag == 4:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")




    
                
    

