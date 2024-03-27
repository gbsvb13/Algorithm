inputnum = 1
while(inputnum != 0):
    inputnum = int(input())
    firstNum = inputnum // 10000
    secondNum = (inputnum // 1000) % 10 
    thirdNum = (inputnum // 100) % 10
    fourthNum = (inputnum // 10) % 10
    LastNum = inputnum % 10
    if inputnum >= 10000 and inputnum <=99999:
        if (firstNum == LastNum) and (fourthNum == secondNum):
            print ("yes")
        else:
            print ("no")
    elif inputnum >= 1000 and inputnum<= 9999:
        if (secondNum == LastNum) and (thirdNum == fourthNum):
            print("yes")
        else:
            print("no")
    elif inputnum >= 100 and inputnum<= 999:
        if (thirdNum == LastNum):
            print("yes")
        else:
            print("no")
    elif inputnum >= 10 and inputnum<= 99:
        if (fourthNum == LastNum):
            print("yes")
        else:
            print("no")
    elif inputnum >= 1 and inputnum <= 9:
        print("yes")   