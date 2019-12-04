# opcode after crash
opcode_temp = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 2,
               9, 19, 23, 1, 9, 23, 27, 2, 27, 9, 31, 1, 31, 5, 35, 2, 35, 9,
               39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 47, 6, 51, 2, 51, 10, 55,
               1, 9, 55, 59, 2, 6, 59, 63, 1, 63, 6, 67, 1, 67, 10, 71, 1, 71,
               10, 75, 2, 9, 75, 79, 1, 5, 79, 83, 2, 9, 83, 87, 1, 87, 9, 91,
               2, 91, 13, 95, 1, 95, 9, 99, 1, 99, 6, 103, 2, 103, 6, 107, 1,
               107, 5, 111, 1, 13, 111, 115, 2, 115, 6, 119, 1, 119, 5, 123,
               1, 2, 123, 127, 1, 6, 127, 0, 99, 2, 14, 0, 0]


def operation(code, val1, val2):
    """Takes the opcode and the values as arguments and returns the result of desired operation
    opcode 1 is for addition
    opcode 2 is for multiplication
    opcode 99 is halt the program"""
    if code == 1:
        return val1 + val2
    elif code == 2:
        return val1 * val2
    elif code == 99:
        return -1


for i in range(0, 100):
    for j in range(0, 100):
        # ************ resetting memory ***********
        opcode = opcode_temp.copy()
        index = 0
        opcode[1] = i
        opcode[2] = j
        # **********************************************
        # moved checking for opcode 99 here to halt the program
        while index <= len(opcode) and opcode[index] != 99:
            # print(operation(opcode[index], opcode[opcode[index + 1]], opcode[opcode[index + 2]]))
            opcode[opcode[index + 3]] = operation(opcode[index], opcode[opcode[index + 1]], opcode[opcode[index + 2]])
            # jumping to next instruction address (always four in this case)
            index += 4
        # print(i,j,opcode[0])
        if opcode[0] == 19690720:
            print("found noun:", i, "verb:", j, "for result:", opcode[0])
            print("Formula answer 100 * noun (" + str(i) + ") + verb (" + str(j) + ") = " + str((100 * i) + j))
            break
    else:
        continue
    break
