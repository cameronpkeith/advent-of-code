def read_input(file_name:str) -> tuple[list, list]:
    left = []
    right = []
    with open(file_name, 'r') as file:
        for line in file:
            split = line.split()
            left.append(int(split[0]))
            right.append(int(split[1]))
    return (left, right)

def solve_part_1(left, right) -> int:
    sum = 0
    for pair in list(zip(left, right)):
        sum += abs(pair[0] - pair[1])
    return sum

def solve_part_2(left, right) -> int:
    counts = {}
    for num in right:
        counts[num] = counts.get(num, 0) + 1

    similarity_score = 0

    for num in left:
        result = counts.get(num, None)
        if result:
            similarity_score = similarity_score + (num * result)
    return similarity_score

def run():
    left, right = read_input("pt1_input.txt")

    left.sort()
    right.sort()

    pt_1_solution = solve_part_1(left, right)
    pt_2_solution = solve_part_2(left, right)

    print(f"Part 1 Solution = {pt_1_solution}")
    print(f"Part 2 Solution = {pt_2_solution}")

if __name__ == "__main__":
    run()
