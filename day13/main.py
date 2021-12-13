import colors
import part1, part2

day = '13'
test1answer = 17
test2answer = None

if __name__ == '__main__':
    print('AdventOfCode 2021 Day ' + day)
    print('\nTESTING')
    print('Part 1: ', end='')
    outcome = part1.part1('day' + day + '/test1.txt')
    if outcome == test1answer:
        print(colors.bcolors.OK + 'Answer: ' + str(outcome) + ', Expected: ' + str(test1answer) + ' [PASSED]' + colors.bcolors.RESET)
    else:
        print(colors.bcolors.FAIL + 'Answer: ' + str(outcome) + ', Expected: ' + str(test1answer) + ' [FAILED]' + colors.bcolors.RESET)
    print('Part 2: ', end='')
    outcome = part2.part2('day' + day + '/test2.txt')
    if outcome == test2answer:
        print(colors.bcolors.OK + 'Answer: ' + str(outcome) + ', Expected: ' + str(test2answer) + ' [PASSED]' + colors.bcolors.RESET)
    else:
        print(colors.bcolors.FAIL + 'Answer: ' + str(outcome) + ', Expected: ' + str(test2answer) + ' [FAILED]' + colors.bcolors.RESET)
    
    print('\nSOLUTIONS')
    print('Solution part 1: ' + str(part1.part1('day' + day + '/input.txt')))
    print('Solution part 2: ' + str(part2.part2('day' + day + '/input.txt')))