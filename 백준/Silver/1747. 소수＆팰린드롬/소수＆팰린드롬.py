import math

inputNum = int(input())

def isPalindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def erasto(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False
    p = 2
    while p * p <= n:
        if isPrime[p]:
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
        p += 1
    return [p for p in range(n + 1) if isPrime[p]]


erastoNumList = erasto(10000000)
endNumList = [integer for integer in erastoNumList if isPalindrome(integer)]


endNumList = [num for num in endNumList if num >= inputNum]



targetNum = min(endNumList)
print(targetNum)
