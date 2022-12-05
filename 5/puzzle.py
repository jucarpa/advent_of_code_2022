sol = {}

def create_stack(line):
    line = line.replace("\n","")
    stack = 0
    ini = 0
    while ini + 3 <= len(line):
        stack += 1
        
        pos_crate = line[ini:ini+3]
        sol_aux = pos_crate.replace(" ","").replace("[","").replace("]","")
        if (sol_aux and ord(sol_aux) >= 65 and ord(sol_aux) <= 90):
            if(stack not in sol):
                sol[stack] = []
            sol[stack].append(sol_aux)
        
        ini += 4

def move(line):
    print(line)
    split_lines = line.split(" ")
    number_items = int(split_lines[1])
    from_items = int(split_lines[3])
    to_items = int(split_lines[5])
    
    moves = sol[from_items][:number_items]
    moves.reverse()
    sol[from_items] = sol[from_items][number_items:]
    sol[to_items] = moves + sol[to_items]

def print_stacks():
    empty_box = "    "
    max_length = 0
    copied_sol = sol.copy()
    for key in copied_sol.keys():
        copied_sol[key] = copied_sol[key].copy()
        aux = len(copied_sol[key])
        if aux > max_length:
            max_length = aux
    
    while max_length > 0:
        aux_line = ""
        for key in copied_sol.keys():
            if len(copied_sol[key]) >= max_length:
                aux_line += "[" + copied_sol[key].pop(0) + "] "
            else: 
                aux_line += empty_box
        print(aux_line)
        max_length -= 1
    
    aux_line = ""
    for key in copied_sol.keys():
        aux_line += f" {key}  "
    print(aux_line)
            
    
moves = False
with open('input.txt', "r") as f:
    for line in f.readlines():
        line = line.replace("\n","")
        if not line:
            moves = True
            aux_sol = {}
            for key in sorted(sol):
                aux_sol[key] = sol[key]
            sol = aux_sol
            print_stacks()
            continue
        if not moves:
            create_stack(line)
        else:
            #input()
            move(line)
            print_stacks()
    
    solution = ""
    for key in sol.keys():
        solution += sol[key][0] if sol[key] else ""
    print(solution)    