with open('inputs/01.txt') as fp:
    puzzle = fp.readline()
    puzzle1 = puzzle + puzzle[0]
    sum1 = 0
    for i in range(len(puzzle1)-1):
        if puzzle1[i] == puzzle1[i+1]:
            sum1 += int(puzzle1[i])
    print(sum1)

    sum2 = 0
    step = int(len(puzzle)/2)
    for i in range(step):
        if puzzle[i] == puzzle[i+step]:
            sum2 += 2*int(puzzle[i])
    print(sum2)
