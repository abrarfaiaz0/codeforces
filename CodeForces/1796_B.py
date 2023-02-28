t = int(input())
for i in range(0,t):
    template = ""
    a = input()
    b = input()
    
    p=0
    temp = ""
    for l in range(0,len(b)):
        
        if b[l] in a[p:]:
            temp = temp + b[l]
            template = template + b[l]
            p+=1
        else:
            template = template + "*"
            continue


    ans = "";
    for l in range(0,len(template)):

        if template[l]!="*":
            ans+=template[l]
        else:
            while (l+1<len(template) and template[l+1]!="*"):
                if(template[l+1]!="*"):
                    ans+="*"
                l+=1
                    
            


    print(ans)
     
