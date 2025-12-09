import sys

def solve(lines):
    pos = 50          # 初始指向 50
    count_zero = 0    # 指向 0 的次数

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            pos = (pos - distance) % 100
        elif direction == "R":
            pos = (pos + distance) % 100
        else:
            raise ValueError(f"Unknown direction: {direction}")

        if pos == 0:
            count_zero += 1

    return count_zero

def solve_part2(lines):
    pos = 50          # 初始指向 50
    count_zero = 0    # 指向 0 的次数
    last_pos = 50

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])



        # if distance more than 100, the count is at least distance // 100
        if distance >= 100:
            count_zero += distance // 100
            distance = distance % 100

        if distance == 0:
            continue

        if direction == "L":
            pos = (pos - distance) % 100
        elif direction == "R":
            pos = (pos + distance) % 100

        if pos < last_pos and direction == 'R' and pos != 0 and last_pos != 0:
            count_zero += 1
        
        if pos > last_pos and direction == 'L' and pos != 0 and last_pos != 0:
            count_zero += 1

        if pos == 0:
            count_zero += 1

        last_pos = pos

    return count_zero



if __name__ == "__main__":
    with open("./input_day1_demo.txt","r") as f:
        data = [line.strip() for line in f if line.strip()]
    print(solve(data))

    print(solve_part2(data))

