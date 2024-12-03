import re
import heapq



def read_input(file_name:str) -> list:
    file_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            file_lines.append(line)
    return file_lines

def process_instruction(instruction: str) -> int:
    val_str = instruction.lstrip("mul(").rstrip(")").split(',')
    l = int(val_str[0])
    r = int(val_str[1])
    return l * r

def solve_part_1(input: str) -> int:
    results = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input)
    
    running_count = 0
    for instruction in results:
        running_count += process_instruction(instruction)

    return running_count

def solve_part_2(input) -> int: 
    conditionals = [ (match.start(), match.group()) for match in re.finditer(r"do\(\)|don't\(\)", input) ]
    instructions = [ (match.start(), match.group()) for match in re.finditer(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input) ]
    combined = list(heapq.merge(conditionals, instructions, key=lambda x: x[0]))

    allowed = True
    sum = 0
    for item in combined:
        compare_val = item[1]
        if compare_val == 'do()':
            allowed = True
        elif compare_val == "don't()":
            allowed = False
        elif compare_val.startswith("mul"):
            if allowed:
                sum += process_instruction(compare_val)
    return sum

def run():
    #data = read_input("test_pt2_input.txt")
    data = read_input("pt1_input.txt")
    merged_str = ''.join(data)

    pt_1_solution = solve_part_1(merged_str)
    pt_2_solution = solve_part_2(merged_str)

    print(f"Part 1 Solution = {pt_1_solution}")
    print(f"Part 2 Solution = {pt_2_solution}")

if __name__ == "__main__":
    run()
