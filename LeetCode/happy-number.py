

def digitsToArray(n):
    arr = []
    while (n != 0):
        temp = n
        n = int(n/10)
        d = temp - n*10
        arr.append(d)
    return arr


def sumOfSquares(arr):
    n = 0
    for i in arr:
        n += i*i
    return n


x = int(input())
print(x)

checked = []

while (sumOfSquares(digitsToArray(x)) not in checked):
    checked.append(sumOfSquares(digitsToArray(x)))
    x = sumOfSquares(digitsToArray(x))
    if (x == 1):
        break

if (x == 1):
    print("true")
else:
    print("false")
