import math


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        ret = "Queue: "
        ret += ", ".join(self.queue)
        return ret

    def __len__(self):
        return len(self.queue)

    def insert(self, value, priority):
        self.queue.append((value, priority))
        self.queue.sort(key=lambda x: x[1])

    def update(self, value, priority):
        for i in range(len(self.queue)):
            (v, p) = self.queue[i]
            if v is value:
                self.queue[i] = (v, priority)
                break
        self.queue.sort(key=lambda x: x[1])

    def get_first(self):
        if len(self.queue) == 0:
            return None
        first = self.queue[0]
        self.queue = self.queue[1:]
        return first[0]


pq = PriorityQueue()
pq.insert("A",1)
pq.insert("B",3)
pq.insert("C",2)
pq.insert("D",5.4)
pq.insert("E",0.5)

top = pq.get_first()
print("Priority:", top)

####
def singleSourceShortest(listOfNodes, S, D): # S = the source/starting point  

    unvisited_set = listOfNodes.copy()

    dist = {}  # map from a node.name => current distance from source
    pred = {}  # not sure? "can be used to rediscover the actual shortest path from each vertex in the graph." 
               # pred is map from a given node to the neighbor with the shortest path

    for node in unvisited_set:
        dist[node.name] = math.inf # this should be infinity
        pred[node.name] = None

    dist[S.name] = 0 # the distance from the start to the start is zero
    pred[S.name] = S.name

    PQ = PriorityQueue()
    for node in listOfNodes:
        PQ.insert(node, dist[node.name])


#### now the iteration
    current_node = S
    while len(PQ): #for each current node, loop through neighbors
        print("outer loop!")
        for key, node in current_node.paths.items():
            # print("K, N", key, node)
            neighbor, distance = node
            # print("PRINTING!", key, neighbor, distance)
            if neighbor not in unvisited_set:
                continue
            #
            tenative_distance_of_neighbor_through_current_node = dist[current_node.name] + distance
            if tenative_distance_of_neighbor_through_current_node < dist[neighbor.name]:
                dist[neighbor.name] = tenative_distance_of_neighbor_through_current_node
                pred[current_node.name] = neighbor.name
                pq.update(neighbor.name, tenative_distance_of_neighbor_through_current_node)
                #pred[neighbor.name] = current_node

        next_current = PQ.get_first()
        next_distance = dist[next_current.name]
        if next_distance == math.inf: #first of two loop escapes, no more reachable nodes
            break
        if D not in unvisited_set:
            break
        current_node = next_current
    # Generate the path of nodes
    # return dist[D.name] #Minimum length
    path = []
    current_name = D.name
    print(dist)
    print(pred)
    while True:
        path.append(current_name)
        current_name = pred[current_name]
        print(current_name)
        if current_name == S.name:
            break
    return path.reverse()


class Node(object):
    def __init__(self, name):
        self.name = name
        self.paths = {}

    def add_node(self, node, distance = 1, reciprocate = True):
        if distance < 0:
            raise Exception("Negative distance relationship!")
        if node.name in self.paths:
            raise Exception("Overwriting node in paths")
        self.paths[node.name] = (node, distance)
        if reciprocate:
            node.add_node(self, distance, reciprocate=False)

class Path(object):
    def __init__(self):
        self.path = []

    def __str__(self):
        ret = "Path: \n"
        cumulative_distance = 0
        for (node, distance) in self.path:
            ret += f"Node {node.name} distance {distance}\n"
        return ret

    def add_node(self, node, distance):
        self.path.append((node, distance))




if __name__ == "__main__":
    #setup nodes
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")


    a.add_node(b)
    b.add_node(c)
    b.add_node(d)
    d.add_node(e)


    #find path
    nodes = [a, b, c, d, e]
    start_node = a
    end_node = e
    path = singleSourceShortest(nodes, start_node, end_node)
    print(path)

