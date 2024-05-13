personNum, num =map(int,input().split())

yosepusArr = []

for i in range(1, personNum + 1):
    yosepusArr.append(i)

resultArr = []
currentIdx = 0
while yosepusArr:
    currentIdx = (currentIdx + num - 1) % len(yosepusArr)
    resultArr.append(yosepusArr.pop(currentIdx))
    
print("<", end = "")
for i in range(len(resultArr)):
    if i == len(resultArr) - 1:
        print(resultArr[i], end="")
    else:
        print(resultArr[i], end=", ")
print(">", end = "")