import random

class Node:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

class DFS:
    def __init__(self):
        self.directions = [
            (1, 0, "Down"),  
            (-1, 0, "Up"),   
            (0, 1, "Right"), 
            (0, -1, "Left")  
        ]
        self.found = False  d
        self.N = 0  
        self.source = None  
        self.goal = None 
        self.path = [] 
        self.topological_order = [] 
        self.grid = [] 

    def generate_grid(self):
        """Generate an N x N grid with random obstacles."""
        self.N = random.randint(4, 7)
        self.grid = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]

        while True:
            source_x, source_y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            goal_x, goal_y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if self.grid[source_x][source_y] == 1 and self.grid[goal_x][goal_y] == 1 and (source_x, source_y) != (goal_x, goal_y):
                break

        self.source = Node(source_x, source_y)
        self.goal = Node(goal_x, goal_y)

    def print_grid(self):
        """Print the grid with source (S) and goal (G) marked."""
        print("\nGenerated Grid:")
        for i in range(self.N):
            for j in range(self.N):
                if (i, j) == (self.source.x, self.source.y):
                    print("S", end=" ")
                elif (i, j) == (self.goal.x, self.goal.y):
                    print("G", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
            print()
        print(f"\nSource: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")

    def dfs(self):
        """Perform DFS traversal from source to goal."""
        stack = [(self.source, [])]
        visited = set()

        while stack:
            u, path_so_far = stack.pop()
            if (u.x, u.y) in visited:
                continue
            
            self.topological_order.append((u.x, u.y))  
            visited.add((u.x, u.y))

            if u.x == self.goal.x and u.y == self.goal.y:
                self.found = True
                self.path = path_so_far + [("Goal", (u.x, u.y))]
                return

            for dx, dy, direction in self.directions:
                v_x, v_y = u.x + dx, u.y + dy
                if 0 <= v_x < self.N and 0 <= v_y < self.N and self.grid[v_x][v_y] == 1 and (v_x, v_y) not in visited:
                    stack.append((Node(v_x, v_y), path_so_far + [(direction, (v_x, v_y))]))

    def display_results(self):
        """Print the DFS results including path and traversal order."""
        if self.found:
            print("\nGoal found!")
            print("Path taken:")
            for move, coord in self.path:
                print(f"{move} -> ({coord[0]}, {coord[1]})")
        else:
            print("\nGoal cannot be reached from the starting block.")

        print("\nTopological Order of Node Traversal:")
        print(" -> ".join(f"({x}, {y})" for x, y in self.topological_order), "-> END")

    def run(self):
        """Execute the entire DFS process."""
        self.generate_grid()
        self.print_grid()
        self.dfs()
        self.display_results()

if __name__ == "__main__":
    dfs = DFS()
    dfs.run()
