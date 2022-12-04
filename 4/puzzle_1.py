def convert_to_int(container):
    return list(map(lambda x: int(x),container))

def parse_line(line):
    line = line.replace("\n", "")
    line = line.split(",")

    c1 = convert_to_int(line[0].split("-"))
    c2 = convert_to_int(line[1].split("-"))
    sol = [c1,c2]
    return sol


def fully_contained(containers):
    c1 = containers[0]
    c2 = containers[1]

    if c1[0] <= c2[0] and c1[1] >= c2[1]:
        return 1
    if c2[0] <= c1[0] and c2[1] >= c1[1]:
        return 1
    return 0

total = 0
with open('input.txt', "r") as f:
    for line in f.readlines():
        line = parse_line(line)
        total += fully_contained(line)
    
    print(total)
        