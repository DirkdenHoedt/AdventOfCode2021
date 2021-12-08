def part2(path):
    global grid
    f = open(path)
    data = f.readlines()

    count = 0

    total = 0

    for i in data:
        sep = i.split(" | ")
        digits = sep[0].split(" ")
        output = sep[1].strip().split(" ")
        digits.sort(key=len)

        for i in range(10):
            s = sorted(digits[i])
            digits[i] = "".join(s)

        for i in range(4):
            s = sorted(output[i])
            output[i] = "".join(s)

        result = convert(digits)

        value = 1000*result[output[0]] + 100*result[output[1]] + 10*result[output[2]] + result[output[3]]
        total += value

    return total
        
def convert(digits):
    result = {digits[0]: 1, digits[1]: 7, digits[2]: 4, digits[9]: 8}
    diff = ""
    for i in digits[2]:
        if i not in digits[0]:
            diff += i

    for i in range(3,6):
        three = True
        for j in digits[1]:
            if j not in digits[i]:
                three = False
        if three:
            result[digits[i]] = 3
        else:
            five = True
            for j in diff:
                if j not in digits[i]:
                    five = False
            if five:
                result[digits[i]] = 5
            else:
                result[digits[i]] = 2

    for i in range(6,9):
        six = False
        for j in digits[0]:
            if j not in digits[i]:
                six = True
        if six:
            result[digits[i]] = 6
        else:
            nine = True
            for j in digits[2]:
                if j not in digits[i]:
                    nine = False
            if nine:
                result[digits[i]] = 9
            else:
                result[digits[i]] = 0
    
    return result
            
            