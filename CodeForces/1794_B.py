t = int(input())
for q in range(t):
    n = int(input())
    s = input()
    s = s.split()
    s = [eval(p) for p in s]
    for i in range(len(s)):
        
        

        if(not i+1>=len(s)):
      
            if(s[i+1]%s[i]==0 or s[i+1]==s[i]):
           
                s[i]+=1
           

        if(not i-1<0):
            
            if(s[i]%s[i-1]==0 or s[i]==s[i-1]):
               
                s[i-1]+=1
                

    for inte in s:
        print(inte, end=" ")

