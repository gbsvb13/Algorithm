king,queen,rook,bis,kn,p = map(int,input().split())

chessArray = []

chessArray.append(1 - king)
chessArray.append(1 - queen)
chessArray.append(2 - rook)
chessArray.append(2 - bis)
chessArray.append(2 - kn)
chessArray.append(8 - p)


for i in range(len(chessArray)):
    print(str(chessArray[i]),end = ' ')