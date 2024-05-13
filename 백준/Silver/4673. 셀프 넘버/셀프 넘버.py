def d(n):
    total = int(n)
    for char in str(n):
        total += int(char)
    return total

numSet = set(range(1,10001))
non_selfNum = set()
for i in range(1,10001):
    non_selfNum.add(d(i))

selfNum = sorted(numSet - non_selfNum)

for num in selfNum:
    print(num)