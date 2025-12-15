
# 第一次犯的错误
# 1. len(lines) 没有 -1，最后一行是符号
# 2. split 默认分割不定数量个空格
# 3. mutiple 的初始值应该是 1 不是 0

def solve_part1(lines):
    # print(lines)
    row = []
    for i in range(0,len(lines)):
        row.append(lines[i].strip().split())
    # print(row)

    result = 0
    for i,sign in enumerate(row[-1]):
        if sign == "+":
            sum = 0
            for j in range(0,len(lines)-1):
                sum += int(row[j][i])
            result += sum
        elif sign == '*':
            multiple = 1
            for j in range(0,len(lines)-1):
                multiple *= int(row[j][i])
            result += multiple
        else:
            raise ValueError
    print(result)

# 思路：倒着来，他们三个都取到空格的时候就是下一道题
def solve_part2(lines):
    row_sign = lines[-1].strip().split()
    lines = lines[:-1]
    datas = []
    digits = []
    problem_indx = -1
    result = 0
    for i in range(0,len(lines[0])):
        # 从后往前遍历字符串
        blank_count = 0
        for j in range(len(lines)):
            bit_num = lines[j][-1-i]
            if bit_num != ' ':
                digits.append(bit_num)
            else:
                blank_count += 1
        
        num = 0
        for multipler, digit in enumerate(digits):
            num += int(digit) * 10 **(len(digits) - multipler - 1)
        if blank_count != len(lines):
            datas.append(num)
        digits = []

        if blank_count == len(lines) or i == (len(lines[0]) - 1):
            # 算题
            sign = row_sign[problem_indx]
            print(datas,sign)
            problem_indx -= 1
            if sign == "+":
                sum = 0
                for data in datas:
                    sum += data
                result += sum
            elif sign == "*":
                multiple = 1
                for data in datas:
                    multiple *= data
                result += multiple
            datas = []
    print(result)
def main():
    with open('./input_day6.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    solve_part1(lines)

    solve_part2(lines)
    
if __name__ == '__main__':
    main()