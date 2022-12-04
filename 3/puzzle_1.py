def find_matches(line):
    size = len(line)
    half =int(size/2)
    rucksack_a = line[:half]
    rucksack_b = line[half:]
    
    matches = []
    iter_list = list(dict.fromkeys(rucksack_a))
    for aux_char in iter_list:
        if aux_char in rucksack_b:
            matches.append(aux_char)
    return matches

def num_value(aux_char):
    if ord(aux_char) - 96 > 0:
                return ord(aux_char) - 96
    else:
        return ord(aux_char) - 38

with open('input.txt', "r") as f:
    matches = []
    for line in f.readlines():
        line = line.replace("\n", "")
        matches = matches + find_matches(line)

    total = sum(num_value(v) for v in matches)
    print(total)
    
    
