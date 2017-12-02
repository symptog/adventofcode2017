with open('inputs/02.txt') as fp:
    puzzle = fp.read()

    sum1 = 0
    for line in puzzle.split('\n'):
        numbers = [int(x) for x in line.split('\t')]
        minimum = min(numbers)
        maximum = max(numbers)
        sum1 += (maximum - minimum)
    print(sum1)

    sum2 = 0
    for line in puzzle.split('\n'):
        numbers = [int(x) for x in line.split('\t')]
        for number1 in numbers:
            for number2 in numbers:
                if number1 == number2:
                    continue
                if number1 % number2 == 0:
                    sum2 += (number1 // number2)
    print(sum2)
