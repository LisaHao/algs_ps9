import sys

def highTower(allBlocks):
    maxHeight = []
    usedBlocks = []
    # initialize max height to height of own box
    # since will at least have height of current box
    for i in range(len(allBlocks)):
        maxHeight.append(allBlocks[i][2])
        usedBlocks.append(i)
    # find the max height for all of the boxes
    for i in range(len(allBlocks)):
        for j in range(0, i): 
            # check against all of the earlier boxes
            # only look at the max heights of boxes that have smaller dimensions that we're currently looking at
            # check if combining with a max height of a stack with one of those boxes will give us a taller stack than the highest height we've found so far
            if allBlocks[j][0] < allBlocks[i][0] and allBlocks[j][1] < allBlocks[i][1] and maxHeight[i] < maxHeight[j] + allBlocks[i][2]:
                # if so, stack our box under the earlier smaller stack
                maxHeight[i] = maxHeight[j] + allBlocks[i][2]
                blocks = [i]
                # add our current box into the list of boxes that make up the height
                if type(usedBlocks[j]) is list:
                    for x in usedBlocks[j]:
                        blocks.append(x)
                else:
                    blocks = [i, usedBlocks[j]]
                usedBlocks[i] = blocks

    bestCombo = 0
    bestBlocks = []
    # go through and find the max height we've found 
    for i in range(len(allBlocks)):
        if maxHeight[i] > bestCombo:
            bestCombo = maxHeight[i]
            bestBlocks = usedBlocks[i]
    print("The tallest tower has", len(bestBlocks), "blocks and a height of", bestCombo)
    outputBlocks = []
    # combine all of the boxes that made up the max height into its own list
    for block in bestBlocks:
        outputBlocks.append(allBlocks[block])
    return outputBlocks, bestCombo



def highestTower(contents):
    blocks = []
    for i in range(len(contents)):
        dimensions = contents[i].split(" ")
        # include all block rotations with different heights
        # smaller dimension first, larger dimension second, height dimension last 
        blocks.append([min(int(dimensions[1]), int(dimensions[2])), max(int(dimensions[1]), int(dimensions[2])), int(dimensions[0])])
        blocks.append([min(int(dimensions[0]), int(dimensions[2])), max(int(dimensions[0]), int(dimensions[2])), int(dimensions[1])])
        blocks.append([min(int(dimensions[0]), int(dimensions[1])), max(int(dimensions[0]), int(dimensions[1])), int(dimensions[2])])
    # sort blocks so that smallest block is first
    blocks.sort()
    # find the max height for the given blocks & the best blocks to make that height
    bestBlocks, maxHeight = highTower(blocks)
    # create output string with maxHeight first
    outputString = str(maxHeight)+ "\n"
    # dimensions of all blocks
    for block in bestBlocks:
        outputString += str(block[0]) + " " + str(block[1]) + " " + str(block[2])
        outputString += "\n"
    return outputString

# open infile.txt
fin = open(sys.argv[1],"r")
# read infile
contents = fin.readlines()
fin.close()
# open outfile
fout = open(sys.argv[2], "w")
# write answer to outfile
fout.write(highestTower(contents[1:]))

