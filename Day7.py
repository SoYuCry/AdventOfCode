# 第一次犯的错误
# 1. 应该用 set 而不是 list 记录 light 的位置，不然可能重复

def main():
    with open('./input_day7.txt', 'r') as f:
        lines = f.read().strip().split('\n')

# 思路：记录管光线/光源的位置，看下一行的对应位置是不是分束器，是的话，更新光线
    lights = set()
    res = 0
    for i,string in enumerate(lines[0]):
        if string == 'S':
            lights.add(i)
    for i in range(1,len(lines)):
        new_lights = set()
        for light in lights:
            if lines[i][light] == '^':
                res += 1
                if light - 1 >= 0:
                    new_lights.add(light-1)
                if light+1 < len(lines[i]):
                    new_lights.add(light+1)
                
            else:
                new_lights.add(light)
        lights = new_lights
        # print(new_lights)
        # print(res)
    print(res)

if __name__ == '__main__':
    main()