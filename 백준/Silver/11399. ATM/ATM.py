person = int(input())
time = list(map(int, input().split()))

sortedtime = sorted(time)

tempTime = []
totalTime = 0
for i in range(len(sortedtime)):
    totalTime += sortedtime[i]
    tempTime.append(totalTime)

tTime = 0
for i in range(len(tempTime)):
    tTime += tempTime[i]

print(tTime)

