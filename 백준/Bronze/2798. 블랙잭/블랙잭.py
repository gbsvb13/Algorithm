#Input UI

numofCards, dealerNum = map(int,input().split())

deck = []

deck = [int(x) for x in input().split()]

for i in range(len(deck)):
    if deck[i] >= dealerNum:
        deck.remove(deck[i])
#dealerNum보다 큰 수를 지움

#Compute UI
validDeck = []
for i in range(len(deck)):
    for j in range(i+1,len(deck)):
        for k in range(i+2,len(deck)):
            if dealerNum >= (deck[i] + deck[j] + deck[k]) and (deck[i]!=deck[j]!=deck[k]):
                validDeck.append(deck[i] + deck[j] + deck[k])
                
mostClose = max(validDeck)

#Output UI
print(mostClose)