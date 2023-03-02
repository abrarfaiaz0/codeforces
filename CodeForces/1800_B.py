import math

t = int(input())
for q in range(t):
    k = int(input().split()[1])
    S = input()
    letters = []
    for letter in S:
        if letter not in letters:
            letters.append(letter)
    burls = 0
    extra = 0
    done=[]
    
    for l in letters:
        if(ord(l)>=97):
            sm = 0
            cp = 0
            for s in S:
                if l == s:
                    sm+=1
                if ord(l)-32==ord(s):
                    cp+=1       
            burls+=min(sm,cp)     
            extra+=math.floor((max(sm,cp)-min(sm,cp))/2)
            done.append(l)  
            done.append(chr(ord(l)-32))  
           
    for l in letters:
        if l not in done:
            cp=0
            for s in S:
                if l == s:
                    cp+=1
            extra+=math.floor(cp/2)  

    print(burls+min(k,extra))
    