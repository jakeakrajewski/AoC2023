class FileNode:
    def __init__(self, file_name, lines, next_file=None):
        self.file_name = file_name
        self.lines = lines
        self.next_file = next_file


file_names = ['SeedToSoil.txt', 'SoilToFertilizer.txt', 'FertilizerToWater.txt', 'WaterToLight.txt', 'LightToTemp.txt', 'TempToHumidity.txt', 'HumidityToLocation.txt']

head = None
current_node = head
node_value = 0
locations = []
seeds = []

all_seeds = []

with open("./Day5/Seeds.txt", 'r') as file:
    for line in file:
        integers = [int(num) for num in line.split()]

        consecutive_tuples = [(integers[i], integers[i + 1]) for i in range(0, len(integers) - 1, 2)]
        seeds.extend(consecutive_tuples)

for file_name in file_names:
    with open("./Day5/" + file_name, 'r') as file:
        lines = [list(map(int, line.split())) for line in file]
        lines = sorted(lines, key=lambda x: x[1])
    
    if head is None:
        head = FileNode(file_name, lines)
        current_node = head
    else:
        current_node.next_file = FileNode(file_name, lines)
        current_node = current_node.next_file

total_seeds = 0
for seed in seeds:
    total_seeds += seed[1]
    
created = 0

for seed in seeds:
    for i in range(seed[1]):
        all_seeds.append(seed[0] + i)
        created += 1
        print(created)
            
        
for seed in all_seeds:
    node_value = seed
    current_node = head
    while current_node is not None:
        found_group = False

        for group in current_node.lines:
            if group[1] <= node_value < group[1] + group[2] - 1:
                node_value = (node_value - group[1]) + group[0]
                current_node = current_node.next_file
                found_group = True
                break

        if not found_group:
            current_node = current_node.next_file

    locations.append(node_value)

print(min(locations))
