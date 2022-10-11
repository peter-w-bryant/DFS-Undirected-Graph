contents = []
instance_len = []
instance_index = []
visited = []

# Read the input
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

# Save the value corresponding to the number of instances
num_instance = int(contents[0])

# Remove the first line of the input and save the remaining lines
graph = contents[1:]

instance_len.append(int(graph[0]))
instance_index.append(0)

# Find the length of each instance and its starting index
while True:
    try:
        new_len = int(graph[sum(instance_len)+len(instance_len)])
        if new_len != None:
            instance_len.append(new_len)
            instance_index.append(instance_index[-1] + instance_len[-2] + 1)
    except IndexError:
        break

# Create a python dictionary for each adjacency list
adj_list = []
adj = {}
for instance in range(num_instance):
    for i in range(instance_index[instance] + 1, instance_index[instance] + instance_len[instance] + 1):
        key = graph[i].split()[0]
        vals = graph[i].split()[1:]
        adj[key] = vals
    if adj != {}:
        adj_list.append(adj)
        adj = {}
    
def DFS(node, adj_list, visit):
    visit.append(node)
    for neighbor in adj_list[node]:
        if neighbor not in visit:
            DFS(neighbor, adj_list, visit)


# Perform DFS on each instance
for instance in range(num_instance):
    visit = []
    for node in adj_list[instance]:
        if node not in visit:
            DFS(node, adj_list[instance], visit)
            if visit not in visited:
                visited.append(visit)

# Print the visited nodes, with a new line after each instance
try:
    sum = 0
    for instance in range(num_instance):
        # Print the visited nodes for each instance
        print(' '.join(visited[instance]))
        sum += instance_len[instance]

except IndexError:
    pass




