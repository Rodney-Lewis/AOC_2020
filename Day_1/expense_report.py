def part1():
    fileInput = open("problem_input.txt", "r")
    textInputArr = fileInput.read().split('\n')
    for x in textInputArr:
        for y in textInputArr:
            if (int(x) + int(y)) == 2020:
                ans = int(x) * int(y)
                txt = "Part1 output: {}"
                print(txt.format(ans))
                break
        if (int(x) + int(y)) == 2020:
            break

def part2():
    fileInput = open("problem_input.txt", "r")
    textInputArr = fileInput.read().split('\n')
    for x in textInputArr:
        for y in textInputArr:
            for z in textInputArr:
                if (int(x) + int(y) + int(z)) == 2020:
                    ans = int(x) * int(y) * int(z)
                    txt = "Part2 output: {}"
                    print(txt.format(ans))
                    break
            if (int(x) + int(y) + int(z)) == 2020:
                break
        if (int(x) + int(y) + int(z)) == 2020:
            break
    
part1()
# Part1 output: 996996

part2()
# Part2 output: 9210402

