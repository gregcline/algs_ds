class Islands:
    def __init__(self, grid):
        self.islands = {
            (x, y): grid[x][y]
            for x in range(0, len(grid))
            for y in range(0, len(grid[0]))
        }

    def add_land(self, x, y):
        if (x, y) in self.islands:
            self.islands[(x, y)] = True

    def count_islands(self):
        visited = set()

        def consume_island(islands, x, y):
            # out of bounds
            if (x, y) not in islands:
                return None
            # not land
            elif islands[(x, y)] == False:
                return None
            # already visited
            elif (x, y) in visited:
                return None
            # visit neighbors
            else:
                visited.add((x, y))
                consume_island(islands, x + 1, y)
                consume_island(islands, x - 1, y)
                consume_island(islands, x, y + 1)
                consume_island(islands, x, y - 1)

        island_count = 0
        for x, y in self.islands.keys():
            if self.islands[(x, y)] and (x, y) not in visited:
                island_count += 1
                consume_island(self.islands, x, y)

        return island_count


grid = [[1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0]]
islands = Islands(grid)
print(islands.count_islands())

