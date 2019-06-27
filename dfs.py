
stack = []
adj_list = [[1], [2, 3], [4, 5], [1], [7], [6], [7], []]
visited = [False for i in range(len(adj_list))]
dist = [0 for i in range(len(adj_list))]

src = 3
dest = 7
for e in adj_list[src]:
    dist[e] += 1
    stack.append(e)

while(len(stack) != 0):
    vertex = stack.pop()
    if visited[vertex]:
        continue
    visited[vertex] = True
    if vertex == dest:
        print "Found destination: %s at dist: %s" % (vertex, dist[vertex])
    print "Visiting: %s" % vertex

    neighbours = list(adj_list[vertex])
    neighbours.reverse()
    for neighbour in neighbours:
        if dist[neighbour] == 0:
            dist[neighbour] = dist[vertex] + 1
        else:
            dist[neighbour] = min(dist[vertex] + 1, dist[neighbour])
        stack.append(neighbour)
    
