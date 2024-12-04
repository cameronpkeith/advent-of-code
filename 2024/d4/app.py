

def read_input(file_name:str) -> list:
    file_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            file_lines.append(line.rstrip())
    return file_lines


def solve_part_1(input: str) -> int:
    pass

def solve_part_2(input) -> int: 
    pass

def possible_dirs(matrix: list[list], x, y):

    for i in range(-1,2):
        for j in range(-1,2):
            m = x+i
            n = y+j

            if m < 0 or m == len(matrix):
                #print("skip m")
                continue
            if n < 0 or n == len(matrix[0]):
                #print("skip n")
                continue
            if i == 0 and j == 0:
                continue

            try: 
                char = matrix[m][n]
                print(f"char: {char}")
            except:
                print(f"exception on: {x+i}, {y+j}")
                continue


def run():
    #data = read_input("test_pt2_input.txt")
    a = read_input("test_input.txt")

    for i, row in enumerate(a):
        for j, col in enumerate(row):
            #print(f"col: {col}")
            if col == 'X':
                print(i, j)
                possible_dirs(a, i, j)
                #break#remove
        #break#remove

    #pt_1_solution = solve_part_1(merged_str)
    #pt_2_solution = solve_part_2(merged_str)

    #print(f"Part 1 Solution = {pt_1_solution}")
    #print(f"Part 2 Solution = {pt_2_solution}")

if __name__ == "__main__":
    run()
