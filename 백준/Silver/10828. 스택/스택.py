import sys
input = sys.stdin.readline
#input UI
runNumber = int(input())
#compute UI
StackList = []
def push(inputNum):
    inputNum = int(inputNum)
    StackList.append(inputNum)
    
def pop() :
    if StackList:
        print(StackList[-1])
        StackList.pop(-1)
    else:
        print(-1)
def size():
    print(len(StackList))

def empty():
    if StackList:
        print(0)
    else:
        print(1)

def top():
    if StackList:
        print(StackList[-1])
    else:
        print(-1)
#output UI
for _ in range(runNumber):
    Commend= input().split()
    if Commend[0] == 'push':
        push(Commend[1])
    elif Commend[0] == 'pop':
        pop()
    elif Commend[0] == 'size':
        size()
    elif Commend[0] == 'empty':
        empty()
    elif Commend[0] == 'top':
        top()
    