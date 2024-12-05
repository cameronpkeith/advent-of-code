

def read_input(file_name:str):
    rules = []
    updates = []
    with open(file_name, 'r') as file:
        for line in file:
            if '|' in line:
                rules.append(line.rstrip())
            elif ',' in line:
                updates.append(line.rstrip())

    return (rules, updates)


def is_update_good(rules, update):
    reordered = False
    i = 0
    while i < len(update):
        num = update[i]
        before = update[:i]
        for b in before:
            if b in rules.get(num,[]):
                while b in before:
                    reordered = True
                    before.remove(b)
                    update.insert(i+1, b)
                    update.remove(b)
                    i -= 1
        i += 1
                
    return update, reordered



def solve(rules, updates) -> int: 
    rm = {}
    for rule in rules:
        split_rules = rule.split('|')
        l = split_rules[0]
        r = split_rules[1]
        if rm.get(l, None):
            rm[l].append(r)
        else:
            rm[l] = [r]

    ordered_sum = 0
    reordered_sum = 0
    for update in updates:
        u = update.split(',')
        result, reordered = is_update_good(rm, u)
        if reordered:
            reordered_sum += int(u[int(len(result)/2)])
        else:
            ordered_sum += int(u[int(len(u)/2)])

    return ordered_sum, reordered_sum


def run():
    rules, updates = read_input("pt1_input.txt")

    pt_1_solution, pt_2_solution = solve(rules, updates)

    print(f"Part 1 Solution = {pt_1_solution}")
    print(f"Part 2 Solution = {pt_2_solution}")

if __name__ == "__main__":
    run()
