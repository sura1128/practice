
class Queue:
    def __init__(self):
        self.queue = list()
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False
    def repr(self):
        return repr(self.queue)

adj_list = [[1, 2, 3], [0, 2, 5], [0, 1, 4], [0, 4], [2, 3], []]
source = 4
dest = 5
dist = [0 for i in range(len(adj_list))]
queue = Queue()
visited = [False for i in range(len(adj_list)+1)]

queue.enqueue(source)
while (not queue.isEmpty()):
    #print "Queue: %s" % queue.repr()
    vertex = queue.dequeue()
    if visited[vertex]:
        #print "Skipping %s" % vertex
        continue
    visited[vertex] = True
    if vertex == dest:
        print "Found destination: %s at dist: %s" % (vertex, dist[vertex])
    print "Visiting: %s" % vertex

    for neighbour in adj_list[vertex]:
        if dist[neighbour] == 0:
            dist[neighbour] = dist[vertex] + 1
        else:
            dist[neighbour] = min(dist[vertex] + 1, dist[neighbour])
        queue.enqueue(neighbour)
