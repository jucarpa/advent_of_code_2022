elves = []
with open('input_1.txt', "r") as f:
    aux = 0
    for line in f.readlines():
        if line == "\n":
            elves.append(aux)
            aux = 0
        else:
            aux = aux + int(line)
elves.sort(reverse=True)
print(elves)
print("----------------------------")
print(elves[0] +elves[1] + elves[2] )


f.close()