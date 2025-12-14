

eight_direction = [(-1,0),(-1,-1),(-1,1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]

# 第一次犯的错误：
# 1. 没有判断，(i,j) 的位置是否是 @
# 2. 没有对 C < 0 做判断，会导致取 line[-1]

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

# def contruct_three_line()


def main():
    # 读入 AoC Day 3 的那一行输入
    with open('./input_day4.txt', 'r') as f:
        lines = f.read().strip().split("\n")
    
    result = 0
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
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()
