solution = {
    "A" : "ROCK",
    "B" : "PAPER",
    "C" : "SCISSORS",
    "X" : "ROCK",
    "Y" : "PAPER",
    "Z" : "SCISSORS"
}

sol_points = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

def points(a, b):
    if solution[a] == solution[b]:
        return 3

    if solution[a] == "ROCK":
        if solution[b] == "PAPER":
            return 6
        else:
            return 0
    
    if solution[a] == "PAPER":
        if solution[b] == "SCISSORS":
            return 6
        else:
            return 0

    if solution[a] == "SCISSORS":
        if solution[b] == "ROCK":
            return 6
        else:
            return 0

sol = 0
with open('input.txt', "r") as f:
    for line in f.readlines():
        aux = line.split(" ")
        a = aux[0]
        b = aux[1][0]
        sol += sol_points[b]
        sol += points(a, b)

print(sol)