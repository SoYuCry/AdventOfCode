
# 第一次写犯的小错误
# 1. int 类型很烦，一不小心就 str 和 int 作比较
# 2. enumerate 的第一个是 indx 第二个是遍历的元素
# 3. 逻辑上犯了一个错误，应该 s > max 的时候才更新最大。不然进度一直往右推，个位数最大的可能会被埋

def part_1(lines):
    result = 0
    for line in lines:
        max_1 = -1
        max_2 = -1
        inx_max = -1
        inx_second = -1
        for i,s in enumerate(line):

            if int(s) > max_1:
                max_1 = int(s)
                inx_second = inx_max
                inx_max = i
        
        if inx_max == len(line)-1:
            inx_max = inx_second
            max_1 = int(line[inx_max])

        for s in line[inx_max+1:]:
            if int(s) >= max_2:
                max_2 = int(s)
        print(max_1*10 + max_2)
        result += max_1*10 + max_2
    
    return result

# 要点：等号问题
# 要点：last_max_index 的更新（没有触发 if 也要想办法更新）
def part_2(lines):
    result = 0
    for line in lines:
        line_value = 0
        for i in range(0,12):
            # 第1位，从 0 找到 len-12+i
            if i == 0:
                left = 0
            else:
                left = last_max_index + 1
            right = len(line) - 12 + i

            best_digit = int(line[left])
            last_max_index = left
            for j in range(left, right+1):
                if int(line[j]) > best_digit:
                    best_digit = int(line[j])
                    last_max_index = j
            line_value = line_value * 10 + best_digit
        print(line_value)
        result += line_value
    return result


def main():
    # 读入 AoC Day 3 的那一行输入
    with open('./input_day3.txt', 'r') as f:
        lines = f.read().strip().split("\n")

    print(part_1(lines))

    print(part_2(lines))


if __name__ == '__main__':
    main()
