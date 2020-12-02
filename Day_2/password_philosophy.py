def part1():
    fileInput = open("problem_input.txt", "r")
    textInputArr = fileInput.read().split('\n')

    totalValidPasswords = 0
    for x in textInputArr:
        y = x.split(" ")

        constraintsArr = y[0].split("-")
        lowerbound = int(constraintsArr[0])
        upperbound = int(constraintsArr[1])

        charPolicy = y[1].split(":")
        char = charPolicy[0]

        password = y[2]
        if(password.count(char) <= upperbound and password.count(char) >= lowerbound):
            totalValidPasswords = totalValidPasswords + 1
        
    print(totalValidPasswords)

def part2():
    fileInput = open("problem_input.txt", "r")
    textInputArr = fileInput.read().split('\n')

    totalValidPasswords = 0
    for x in textInputArr:
        y = x.split(" ")

        constraintsArr = y[0].split("-")
        pos1 = int(constraintsArr[0])
        pos2 = int(constraintsArr[1])

        charPolicy = y[1].split(":")
        char = charPolicy[0]

        password = y[2]
        
        if((password[pos1 - 1] == char and password[pos2 - 1] != char) or (password[pos1 - 1] != char and password[pos2 - 1] == char)):
            totalValidPasswords = totalValidPasswords + 1

    print(totalValidPasswords)

part1()
# 569

part2()
# 346