def read_input(file_name:str) -> tuple[list, list]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            split = line.split()
            data.append([int(x) for x in split])
    return data

def is_report_safe(report: list):
    return ( 
        #ascending
        all(report[i] <= report[i + 1] and report[i+1] - report[i] in range(1,4) for i in range(len(report) - 1)) 
            or 
        #descending
        all(report[i] >= report[i + 1] and report[i] - report[i+1] in range(1,4) for i in range(len(report) - 1)))
    

def solve_part_1(data) -> int:
    count = 0
    for report in data:
        count = count + 1 if is_report_safe(report) else count

    return count

def solve_part_2(data) -> int:
    count = 0
    for report in data:
        if is_report_safe(report):
            count = count + 1
        else:
            safe = False
            for i in range(len(report)):
                copy_list = report[:]
                copy_list.pop(i)
                safe = is_report_safe(copy_list)
                if safe:
                    count = count + 1
                    break
    return count

def run():
    data = read_input("pt1_input.txt")


    pt_1_solution = solve_part_1(data)
    pt_2_solution = solve_part_2(data)

    print(f"Part 1 Solution = {pt_1_solution}")
    print(f"Part 2 Solution = {pt_2_solution}")

if __name__ == "__main__":
    run()
