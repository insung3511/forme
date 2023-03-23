arraySize           = int(input())
xPoints, yPoints    = map(int, input().split())
mapPoints = []

def mapPrinter(mapList):
    for i in range(len(mapList)):
        print(mapList[i])

# Create Map list
for i in range(arraySize):
    tempList = []
    for j in range(arraySize):
        tempList.append(0)
    mapPoints.append(tempList)

# Modify map list
mapPoints[xPoints - 1][yPoints - 1] = 1
mapPrinter(mapPoints)