def part1(distanceRight, distanceDown, lengthOfInputRow):
    fileInput = open("problem_input.txt", "r")
    textInputArr = fileInput.read().split('\n')

    #Change to the length of a single row of the input
    currentPosX = 0
    treesPassed = 0

    for currentPosY in range(distanceDown, len(textInputArr), distanceDown):
        currentPosX += distanceRight
        if(textInputArr[currentPosY][currentPosX % lengthOfInputRow] == "#"):
            treesPassed+= 1
    print(treesPassed)
    return treesPassed

def part2():
    r1d1 = part1(1, 1, 31)
    r3d1 = part1(3, 1, 31) #284
    r5d1 = part1(5, 1, 31)
    r7d1 = part1(7, 1, 31)
    r1d2 = part1(1, 2, 31)
    print(r1d1 * r3d1 * r5d1 * r7d1 * r1d2)

part2()
#3510149120