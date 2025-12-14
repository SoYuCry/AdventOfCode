

eight_direction = [(-1,0),(-1,-1),(-1,1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]

# 第一次犯的错误：
# 1. 没有判断，(i,j) 的位置是否是 @
# 2. 没有对 C < 0 做判断，会导致取 line[-1]

# part2 犯的错误
# 1. read 可以优化，从 lines = f.read().strip().split("\n") 改为 lines = [list(line.rstrip('\n')) for line in f]
#    这样做的好处是，可以通过 lines[i][j] = '.' 赋值
# 2. 理解错题意，本来以为是 remove 一个就 update 一次，但是其实是根据快照全部 remove 掉才进行下一个 round
# 3. while 循环一开始有点点懵，还有 removeables = [] 的重置位置应该在 remove 动作之后，差点搞错。以及 for x in xs 是允许 xs 为空的

def solve_part1(three_lines,i):

    # the line uppper in the (i,j)
    # the line of (i.j)
    # the line lower in the (i,j)

    # so (i,j) is always be (1,j)
    count = 0
    for direction in eight_direction:
        r = 1+direction[0]
        c = i + direction[1]

        if c < 0 or c >= len(three_lines[(r)]):
            continue

        if three_lines[(r)][(i+direction[1])] == '@':
            count += 1
        if count >= 4:
            return False
    return True


def main():
    with open('./input_day4.txt', 'r') as f:
        lines = [list(line.rstrip('\n')) for line in f]
    
    result = 0
    removeables = []
    while True:
        for removeable in removeables:
            lines[removeable[0]][removeable[1]] = '.'
        removeables = []
        for j in range(0,len(lines)):
            if j-1 >= 0:
                line1 = lines[j-1]
            else:
                line1 = "."*len(lines[j])
            line2 = lines[j]
            if j+1 >= len(lines):
                line3 = '.'*len(lines[j])
            else:
                line3 = lines[j+1]
            
            three_lines = [line1,line2,line3]
            for i in range(0,len(lines[j])):

                if lines[j][i] != '@':
                    continue

                if solve_part1(three_lines,i):
                    # if removeable, add into stroe, update all lines and solve again
                    result += 1
                    removeables.append([j,i])

        if len(removeables) == 0:
            break
    
    print(result)

if __name__ == '__main__':
    main()
