
# 第一次写犯的小错误
# 1. int 类型很烦，一不小心就 str 和 int 作比较
# 2. enumerate 的第一个是 indx 第二个是遍历的元素
# 3. 逻辑上犯了一个错误，应该 s > max 的时候才更新最大。不然进度一直往右推，个位数最大的可能会被埋

def main():
    # 读入 AoC Day 3 的那一行输入
    with open('./input_day3.txt', 'r') as f:
        lines = f.read().strip().split("\n")

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
    
    print(result)
            

if __name__ == '__main__':
    main()
