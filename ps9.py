import sys

def highTower(allBlocks):
    maxHeight = []
    usedBlocks = []
    # since will at least use own boxes
    for i in range(len(allBlocks)):
        maxHeight.append(allBlocks[i][2])
        usedBlocks.append(i)
    for i in range(len(allBlocks)):
        if i == 0:
            maxHeight.append(allBlocks[0][2])
            usedBlocks.append(allBlocks[0])
        else:
            for j in range(0, i): 
                # check if second dimension is bigger than the one we want to stack
                if allBlocks[j][0] < allBlocks[i][0] and allBlocks[j][1] < allBlocks[i][1] and maxHeight[i] < maxHeight[j] + allBlocks[i][2]:
                    maxHeight[i] = maxHeight[j] + allBlocks[i][2]
                    blocks = [i]
                    if type(usedBlocks[j]) is list:
                        for x in usedBlocks[j]:
                            blocks.append(x)
                    else:
                        blocks = [i, usedBlocks[j]]
                    usedBlocks[i] = blocks

    bestCombo = 0
    bestBlocks = []
    for i in range(len(allBlocks)):
        if maxHeight[i] > bestCombo:
            bestCombo = maxHeight[i]
            bestBlocks = usedBlocks[i]
    print("The tallest tower has", len(bestBlocks), "blocks and a height of", bestCombo)
    outputBlocks = []
    for block in bestBlocks:
        outputBlocks.append(allBlocks[block])
    return outputBlocks, bestCombo



def highestTower(contents):
    blocks = []
    for i in range(len(contents)):
        dimensions = contents[i].split(" ")
        # all heights
        # smaller dimension first, larger dimension second, height dimension last 
        blocks.append([min(int(dimensions[1]), int(dimensions[2])), max(int(dimensions[1]), int(dimensions[2])), int(dimensions[0])])
        blocks.append([min(int(dimensions[0]), int(dimensions[2])), max(int(dimensions[0]), int(dimensions[2])), int(dimensions[1])])
        blocks.append([min(int(dimensions[0]), int(dimensions[1])), max(int(dimensions[0]), int(dimensions[1])), int(dimensions[2])])
    # sort blocks so that largest block is first, makes easier to iterate through
    blocks.sort()
    bestBlocks, bestHeight = highTower(blocks)
    outputString = str(bestHeight)+ "\n"
    for block in bestBlocks:
        outputString += str(block[0]) + " " + str(block[1]) + " " + str(block[2])
        outputString += "\n"
    return outputString

fin = open(sys.argv[1],"r")
contents = fin.readlines()
fin.close()
fout = open(sys.argv[2], "w")
fout.write(highestTower(contents[1:]))

