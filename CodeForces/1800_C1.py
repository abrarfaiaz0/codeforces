def find_max(arr):
    max = 0
    for e in arr:
        if e >= max:
            max = e
    return max

t = int(input())
for q in range(t):
    n = int(input())
    s = input()
    s = s.split()
    p = 0
    s = [eval(i) for i in s]
    for i in range(len(s)):
        m = 0
        if(s[i]==0):
            m = find_max(s[0:i])
            ind = s.index(m)
            s = s[0:ind]+[0]+s[ind+1:]
            p += m
    print(p)



