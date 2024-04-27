import heapq
import math
import matplotlib.pyplot as plt

'''
Note:
    0 for reachable,
    1 for obstacle,
    2 for stream,
    3 for dessert
'''

'''
Construct graph
'''

'''
Configuration
'''
COSTS = {
    0: 0, #reachable
    1: float('inf'), #obstacle
    2: 2, #stream
    3: 4, #dessert
}

COLORS = {
    0: 'white',
    1: 'gray',
    2: 'blue',
    3: 'wheat',
}

#graph1
'''width = 17
height = 14
graph = [[0 for j in range(height)] for i in range(width)]
obstacles = [(6,8), (6,7), (7,6), (7,5), (7,4), (8,4), (8,3), (8,2)]
for x, y in obstacles:
    graph1[x][y] = 1
start = (3, 5)
target = (14, 4)'''

#graph2
width = 40
height = 20
graph = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0],
    [1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,1],
    [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3],
    [2,0,0,0,0,0,0,0,0,1,0,0,0,3,3,3,3,3,3,3],
    [2,2,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3],
    [2,2,2,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3],
    [0,2,2,2,2,0,1,0,1,0,0,0,3,3,3,3,3,3,3,3],
    [0,0,2,2,2,2,2,0,2,2,2,2,3,3,3,3,2,3,3,3],
    [0,0,0,2,2,2,2,2,0,2,2,2,2,2,2,2,3,2,3,3],
    [0,0,0,0,0,2,2,2,2,0,2,2,2,2,2,3,3,3,2,3],
    [0,0,0,0,0,0,0,0,2,2,0,2,2,0,0,3,3,3,3,3],
    [0,0,0,0,0,0,0,0,0,2,1,0,1,0,0,0,3,3,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3],
]
start = (4, 9)
target = (35, 19)

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

class AStar:
    def __init__(self, width, height, graph):
        self.graph = graph
        self.width = width
        self.height = height

    def heuristic(self, node, target):
        return math.sqrt((node.position[0]-target.position[0])**2 + 
                (node.position[1]-target.position[1])**2)
    
    def is_in_graph(self, node):
        return 0 <= node[0] < width and 0 <= node[1] < height

    def get_neighbors(self, node):
        neighbors = []
        x, y = node.position
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = x+dx, y+dy
            if self.is_in_graph((new_x, new_y)):
                neighbor = Node((new_x, new_y), node)
                neighbor.g = node.g + 1 + COSTS[self.graph[new_x][new_y]]
                neighbors.append(neighbor)
        for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
            new_x, new_y = x+dx, y+dy
            if self.is_in_graph((new_x, new_y)):
                neighbor = Node((new_x, new_y), node)
                neighbor.g = node.g + math.sqrt(2) + COSTS[self.graph[new_x][new_y]]
                neighbors.append(neighbor)
        return neighbors
    
    def construct_path(self, node):
        #Note: you can accumulate total_cost here
        path = []
        cost = node.g
        while node:
            path.append(node.position)
            node = node.parent
        return path[::-1], cost

    def astar(self, start, target):
        open_list = []
        closed_set = set()
        start_node = Node(start)
        target_node = Node(target)
        start_node.g = 0
        start_node.h = self.heuristic(start_node, target_node)
        start_node.f = start_node.g + start_node.h
        heapq.heappush(open_list, start_node)

        while open_list:
            current_node = heapq.heappop(open_list)
            if current_node.position == target_node.position:
                return self.construct_path(current_node)

            closed_set.add(current_node.position)
            for neighbor in self.get_neighbors(current_node):
                if neighbor.position in closed_set:
                    continue
                neighbor.h = self.heuristic(current_node, target_node)
                neighbor.f = neighbor.g + neighbor.h
                heapq.heappush(open_list, neighbor)

        return None, None

    def bi_astar(self, start, target):
        forward_open_list = []
        backward_open_list = []
        forward_closed_set = set()
        backward_closed_set = set()
        
        start_node = Node(start)
        target_node = Node(target)
        start_node.g = 0
        start_node.h = self.heuristic(start_node, target_node)
        start_node.f = start_node.g + start_node.h

        target_node.g = COSTS[self.graph[target[0]][target[1]]]
        target_node.h = self.heuristic(target_node, start_node)
        target_node.f = target_node.g + target_node.h

        heapq.heappush(forward_open_list, start_node)
        heapq.heappush(backward_open_list, target_node)

        while forward_open_list and backward_open_list:
            forward_current_node = heapq.heappop(forward_open_list)
            backward_current_node = heapq.heappop(backward_open_list)
            
            if forward_current_node.position in backward_closed_set:
                backward_node_list = []
                for node in backward_open_list:
                    if forward_current_node.position == node.position:
                        backward_node_list.append(node)
                backward_node_list.sort(key=lambda node: node.g)
                backward_node = backward_node_list[0]
                forward_path, forward_cost = self.construct_path(forward_current_node)
                backward_path, backward_cost = self.construct_path(backward_node)
                return forward_path, backward_path, forward_cost+backward_cost
            
            forward_closed_set.add(forward_current_node.position)
            for neighbor in self.get_neighbors(forward_current_node):
                if neighbor.position in forward_closed_set:
                    continue
                neighbor.h = self.heuristic(forward_current_node, target_node)
                neighbor.f = neighbor.g + neighbor.h
                heapq.heappush(forward_open_list, neighbor)
            
            backward_closed_set.add(backward_current_node.position)
            for neighbor in self.get_neighbors(backward_current_node):
                if neighbor.position in backward_closed_set:
                    continue
                neighbor.h = self.heuristic(backward_current_node, start_node)
                neighbor.f = neighbor.g + neighbor.h
                heapq.heappush(backward_open_list, neighbor)

        return None, None

    def plot_graph(self):
        for i in range(self.height+1):
            plt.plot([0, width], [i, i], 'k-', lw=2)
        for i in range(self.width+1):
            plt.plot([i, i], [0, height], 'k-', lw=2)
        
        for i in range(self.width):
            for j in range(self.height):
                self.plot_rectangle(i, j, COLORS[self.graph[i][j]])

        plt.axis('equal')
        plt.axis('off')
    
    def plot_rectangle(self, x, y, color):
        plt.fill([x, x+1, x+1, x, x], [y, y, y+1, y+1, y], color=color)

    def plot_path(self, path, color):
        for p in path:
            self.plot_rectangle(p[0], p[1], color=color)

    def plot_start_target(self, start, target):
        self.plot_rectangle(start[0], start[1], 'black') 
        self.plot_rectangle(target[0], target[1], 'black')
        
'''
Main function
'''
if __name__ == '__main__':
    
    '''astar = AStar(width, height, graph)
    path, cost = astar.astar(start, target)
    print(cost)
    astar.plot_graph()
    astar.plot_path(path, 'green')
    astar.plot_start_target(start, target)
    plt.show()'''
    
    astar = AStar(width, height, graph)
    path_s, path_t, cost = astar.bi_astar(start, target)
    print(cost)
    astar.plot_graph()
    astar.plot_path(path_s, 'green')
    astar.plot_path(path_t, 'red')
    astar.plot_start_target(start,target)
    plt.show()
    #print(path1)
    #print(path2)'''
