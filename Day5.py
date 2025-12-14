
# 第一次犯的错误
# 1. 直接暴力解，把 range 中的 id 全部存 list，然后 id for 循环检查是否 in list。实际上爆显存
# 2. 没有注意到 demo range 的范围是有重叠的。
# 开始尝试直接用 range 判断，并处理范围重叠情况。

# 第二次犯的错误：
# 1. 二分法忘完了，写了死循环
# 2. None 和 0 都会通过 if not hit_index，改为 return -1
# 3（最重要）：没有处理跨越多个区间

# gpt 用 merge_ranges 直接合并区间，甚至是多个。。。省了一大段代码
# 同时，直接保存 (start_id, end_id)，完全没必要在外面 split


def split_start_end(range_str):
    range_start = int(range_str.strip().split('-')[0])
    range_end = int(range_str.strip().split('-')[1])
    return(range_start,range_end)

def merge_ranges(ranges):
    # ranges: list of (start, end)
    ranges.sort(key=lambda x: x[0])
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged  # list of [start, end]

def judge_in_some_range(ranges,id):
    # find all stars, 二分法 find the first start bigger than id, return i-1
    # if the conressponding end is bigger than id, return this range
    start_ids = []
    end_ids = []
    for start_id, end_id in ranges:
        start_ids.append(start_id)
        end_ids.append(end_id)
    
    # 二分法:找到第一个小于等于 id 的 start_id
    l = 0
    r = len(start_ids)
    while True:
        mid = (l+r)//2

        if mid + 1 >= len(start_ids) or l==r:
            break
                
        if start_ids[mid] <= id and start_ids[mid+1] > id:
            break
        
        if start_ids[mid] < id:
            l = mid
        else:
            r = mid
    
    if end_ids[mid] >= id and start_ids[mid] <= id:
        return mid
    
    return -1

def solve_part2(ranges):
    sum = 0
    for start_id, end_id in ranges:
        sum += end_id - start_id + 1
    return sum

def main():
    with open('./input_day5.txt', 'r') as f:
        fresh_ranges_strs = []
        available_ids = []

        available_start = False

        for line in f:
            if line == '\n':
                available_start = True
                continue
            if available_start:
                available_ids.append(int(line.strip().split('\n')[0]))
            else:
                range_start_id,range_end_id = split_start_end(line.strip().split('\n')[0])
                fresh_ranges_strs.append((range_start_id,range_end_id))

    # 第二次的错误写法记录在这里，被 GPT 5 行秒杀的 merge，我竟然写的非常复杂，而且还是错误的。无法 handle 当前区间是 10-14，但是 new range 是 5-20 的情况。
    # 这种情况根本不需要 hit 任何 range。

    # # merge ranges: the ideal ranges is whoes start1-end1-strart2-end2-...strartn-endn is in increasing
    # # if new_range_start is in some range, the end should update to be max(range_end,new_range_end)
    # # then, if new_range_end is in, the strart should update as min(range_start,new_range_strart)
    # # the function to judge whether new_range_start is in somerange is the same with whether avaiable_id in some range
    # ranges = []
    # for fresh_ranges_str in fresh_ranges_strs:
    #     if len(ranges) == 0:
    #         ranges.append(fresh_ranges_str)
    #         continue
    #     new_rang_start, new_rang_end = split_start_end(fresh_ranges_str)
        
    #     hit_indx = judge_in_some_range(ranges, new_rang_start)

    #     # 如果没有 hit，
    #     if hit_indx == -1:
    #         ranges.append(fresh_ranges_str)
    #         continue
        
    #     hit_range = ranges[hit_indx]
    #     hit_range_start, hit_range_end = split_start_end(hit_range)

    #     if new_rang_end > hit_range_end and new_rang_start <= hit_range_end:
    #         ranges[hit_indx] = str(hit_range_start)+'-'+str(new_rang_end)


    fresh_ranges_strs = merge_ranges(fresh_ranges_strs)
    result = 0
    # print(fresh_ranges_strs)
    for available_id in available_ids:
        hit_indx = judge_in_some_range(fresh_ranges_strs, available_id)

        if hit_indx == -1:
            continue
        print(available_id)
        result += 1

    print(result)

    print(solve_part2(fresh_ranges_strs))
        


if __name__ == '__main__':
    main()
