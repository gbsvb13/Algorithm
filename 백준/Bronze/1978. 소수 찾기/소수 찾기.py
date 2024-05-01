

roopNum = int(input())
nums = list(map(int,input().split()))

numCount = 0

for i in range(roopNum):
    if nums[i] == 1:
        continue
    elif nums[i] == 2:
        numCount+= 1
    else:
        for j in range(2,nums[i]):
            if nums[i] % j == 0:
                break
            else:
                if j == nums[i] - 1:
                    numCount+= 1

print(numCount)
            
            
            
