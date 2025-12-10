# 思路：
# 1. 符合条件数字一定是偶数位
# 2. 将数字拆成两半，A = A1 A2；B = B1 B2
# 3. 遍历寻找 A1-B1 与 A2-B2 的并集
# 4. 但是 A1 可能是 3 位，B1 可能是 5 位。所以拆的时候，应该以 B 为准

# 第一次修改，犯的几个小错误

# 10^len   # 这是按位异或，不是 10 的 len 次幂
# 10**len  # 才是幂

# with open('./input_day2.txt','r') as f:
#     text = f.read() # 漏掉了.read()

# strings = text.strip().split(",") # split 是 stripe 的一个方法

def parse_ranges(line):
    """
    把一整行形如：
    11-22,95-115,998-1012,...
    解析成 [(11, 22), (95, 115), ...]
    """
    ranges = []
    for part in line.strip().split(','):
        part = part.strip()
        if not part:
            continue
        a_str, b_str = part.split('-')
        ranges.append((int(a_str), int(b_str)))
    return ranges


def sum_invalid_ids(ranges):
    """
    给定一组区间，计算所有“由某个数字串重复两次组成”的 ID 之和。
    对每个区间 [L, R]：
      - 只考虑偶数位数 digits = 2, 4, 6, ...
      - digits = 2k，对应半段长度 k
      - 设 base = 10^k，则整个数 X = h * base + h = h * (base + 1)
      - 约束 1：L <= X <= R
      - 约束 2：h 是 k 位数（无前导 0）
    """
    total = 0

    for L, R in ranges:
        max_digits = len(str(R))

        # 只考虑偶数位数
        for digits in range(2, max_digits + 1, 2):
            k = digits // 2
            base = 10 ** k            # 用来拼接：X = h * base + h
            denom = base + 1          # X = h * (base + 1)

            # h 必须是 k 位数（无前导 0）
            h_min_kdigits = 10 ** (k - 1)
            h_max_kdigits = 10 ** k - 1

            # 区间约束：L <= h * denom <= R
            # => ceil(L/denom) <= h <= floor(R/denom)
            h_min_range = (L + denom - 1) // denom  # 上取整
            h_max_range = R // denom                # 下取整

            # 两类约束取交集
            h_from = max(h_min_kdigits, h_min_range)
            h_to = min(h_max_kdigits, h_max_range)

            if h_from <= h_to:
                for h in range(h_from, h_to + 1):
                    x = h * base + h
                    total += x

    return total


def is_invalid_part2(s: str) -> bool:
    # 写法 A：可读
    n = len(s)
    if n <= 1:
        return False

    for block_len in range(1, n // 2 + 1):
        if n % block_len != 0:
            continue
        k = n // block_len
        if k < 2:
            continue
        block = s[:block_len]
        if block * k == s:
            return True

    return False

    # 若想用写法 B，把上面函数体替换成这一行即可：
    # return len(s) > 1 and s in (s + s)[1:-1]


def sum_invalid_ids_part2(ranges):
    total = 0
    for L, R in ranges:
        for n in range(L, R + 1):
            s = str(n)
            if is_invalid_part2(s):
                total += n
    return total



def main():
    # 读入 AoC Day 2 的那一行输入
    with open('./input_day2.txt', 'r') as f:
        line = f.read().strip()

    ranges = parse_ranges(line)
    result1 = sum_invalid_ids(ranges)

    result2 = sum_invalid_ids_part2(ranges)


    print(result1)
    print(result2)


if __name__ == '__main__':
    main()
