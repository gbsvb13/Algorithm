listLen = int(input())
numList = list(map(int, input().split()))
targetNum = int(input())

count = 0
numList.sort()
Start = 0
end = listLen - 1
while Start < end:
    sum = numList[Start] + numList[end]
    if sum == targetNum:
        count += 1
        Start += 1
        end -= 1
    elif sum < targetNum:
        Start += 1
    else:
        end -= 1

print(count)
