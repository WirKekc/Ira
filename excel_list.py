index = 0
with open('list.txt') as a:
    for line in a:
        index += 1
        if index%8 == 1:
            print(index, line)
