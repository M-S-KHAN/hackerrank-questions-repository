
def parse_input():
    num_of_cubes = int(input())
    cubes = [int(i) for i in input().split()]
    return num_of_cubes, cubes    
    
cases = int(input())

for i in range(cases):
    
    num_of_cubes, cubes = parse_input()
    
    start = 0
    end = num_of_cubes - 1
    
    if cubes[end] > cubes[start]:
        last_added = cubes[end]
        end -= 1
    else:
        last_added = cubes[start]
        start += 1
        
    is_broken = False
    for i in range(num_of_cubes - 1):
        if cubes[end] > cubes[start]:
            if cubes[end] > last_added:
                print("No")
                is_broken = True
                break
            last_added = cubes[end]
            end -= 1
        else:
            if cubes[start] > last_added:
                print("No")
                is_broken = True
                break
            last_added = cubes[start]
            start += 1

    if not is_broken:
        print("Yes")
    