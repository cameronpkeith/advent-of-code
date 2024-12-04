

def read_input(file_name:str) -> list:
    file_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            file_lines.append(line.rstrip())
    return file_lines

def find_all_xmas_in_dir(matrix, x, y, offx, offy, running_chars, next_char) -> int:
    m = x+offx
    n = y+offy
    char = matrix[x+offx][y+offy]

    if m < 0 or m == len(matrix):
        return 0
    if n < 0 or n == len(matrix[0]):
        return 0

    if char == next_char:
        if running_chars == "XMA":
            return 1
        else:
            xmas = "XMAS"
            nc = xmas[xmas.find(next_char)+1]
            return find_all_xmas_in_dir(matrix, x+offx, y+offy, offx, offy, running_chars+char, nc)
    else:
        return 0

def find_all_xmas(matrix: list[list], x, y) -> int:

    running_count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            m = x+i
            n = y+j

            if m < 0 or m == len(matrix):
                continue
            if n < 0 or n == len(matrix[0]):
                continue
            if i == 0 and j == 0:
                continue

            try: 
                char = matrix[m][n]
                if char == 'M':
                    running_count += find_all_xmas_in_dir(matrix, m, n, i, j, "XM", 'A' )
                     
            except Exception as e:
                print(e)
                print(f"exception on: {m}, {n}")
                continue

    return running_count


def solve_part_1(input: list[list]) -> int:
    running_count = 0

    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == 'X':
                running_count += find_all_xmas(input, i, j)

    return running_count

def solve_part_2(input) -> int: 
    pass


def run():
    #data = read_input("test_pt2_input.txt")
    a = read_input("pt1_input.txt")

    pt_1_solution = solve_part_1(a)
    #pt_2_solution = solve_part_2(merged_str)

    print(f"Part 1 Solution = {pt_1_solution}")
    #print(f"Part 2 Solution = {pt_2_solution}")

if __name__ == "__main__":
    run()
