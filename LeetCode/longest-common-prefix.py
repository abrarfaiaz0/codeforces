strs = ["flower","flow","flight"]
index = 0
min_length = 200
flag = False
word = ""
print(len(strs))

for s in strs:
    if len(s)<=min_length:
        min_length = len(s)
        word = s
print(word)


for i in range(min_length):
    
    if flag == True:
        break
    index=i 
    for s in strs:
        print(i,word[i],s[i])
        if word[i]!=s[i]:
            flag = True
            index-=1
            break
    


print(word[0:index+1])


    

  
