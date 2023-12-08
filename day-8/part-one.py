#!/opt/homebrew/bin/ python3

with open("input.txt") as f:
    # Extract directions into list and strip newline
    dirs = list(f.readline().strip())

    f.readline() # Skip line 2
    
    lookups = dict()

    while line := f.readline():
        line = line.strip()

        lookups[line[0:3]] = {
            "L": line[7:10],
            "R": line[12:15]
        }

current = "AAA"
end = "ZZZ"
i = 0

while current != end:
    current = lookups[current][dirs[i % len(dirs)]]
    i += 1

print(i)
