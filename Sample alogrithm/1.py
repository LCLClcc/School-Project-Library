def a_star_search(start, end):
    """
    寻路方法，找到终点返回终点grid,否则返回None
    :param start:
    :param end:
    :return:
    """

    # 待访问的格子
    open_list = []
    # 已访问的格子
    close_list = []
    # 把起点加入open_list中
    open_list.append(start)
    # 主循环，每一轮检查一个当前方格节点
    while len(open_list) > 0:
        # 在open_list中查找F值最小的节点作为当前方格节点
        current_grid = find_min_gird(open_list)
        # 将F值最小的节点从open_list中删除
        open_list.remove(current_grid)
        # 将F值最小的节点加入到close_list中
        close_list.append(current_grid)
        # 找到当前节点的所有领近节点
        neighbors = find_neighbors(current_grid, open_list, close_list)
        for grid in neighbors:
            if grid not in open_list:
                # 如果当前节点不在open_list中，标记为父节点，并放入open_list中
                grid.init_grid(current_grid, end)
                open_list.append(grid)
            # 如果终点在open_list中，直接返回终点格子
            for grid in open_list:
                if (grid.x == end.x) and (grid.y == end.y):
                    return grid
        # 遍历完open_list,仍然找不到终点，说明还没到终点，返回空
    return None


def find_min_gird(open_list=[]):
    """
    寻找F值最小的格子的方法
    :param open_list:
    :return:
    """
    temp_grid = open_list[0]
    for grid in open_list:
        if grid.f < temp_grid.f:
            temp_grid = grid
    return temp_grid


def find_neighbors(grid,open_list=[],close_list=[]):
    """
    寻找当前格子领近格子的方法
    :param grid:
    :param open_list:
    :param close_list:
    :return:
    """
    grid_list = []
    if is_valid_grid(grid.x,grid.y-1,open_list,close_list):
        grid_list.append(Grid(grid.x,grid.y-1))
    if is_valid_grid(grid.x,grid.y+1,open_list,close_list):
        grid_list.append(Grid(grid.x,grid.y+1))
    if is_valid_grid(grid.x-1,grid.y,open_list,close_list):
        grid_list.append(Grid(grid.x-1,grid.y))
    if is_valid_grid(grid.x+1,grid.y,open_list,close_list):
        grid_list.append(Grid(grid.x+1,grid.y))
    return grid_list


def is_valid_grid(x,y,open_list=[],close_list=[]):
    """
    判断是否越界和障碍物方法
    :param x:
    :param y:
    :param open_list:
    :param close_list:
    :return:
    """
    # 判断是否越界
    if x < 0 or x >= len(MAZE) or y < 0 or y >= len(MAZE[0]):
        return False
    # 判断是否有障碍物
    if MAZE[x][y] == 1:
        return False
    # 是否已经在open_list中
    if contain_grid(open_list,x,y):
        return False
    # 是否已经在close_list中
    if contain_grid(close_list,x,y):
        return False
    return True


def contain_grid(grids, x, y):
    for grid in grids:
        if (grid.x == x) and (grid.y == y):
            return True
    return False


class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None

    def init_grid(self, parent, end):
        self.parent = parent
        if parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 1
        self.h = abs(self.x - end.x) + abs(self.y - end.y)
        self.f = self.g + self.h


# 迷宫地图
MAZE = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
        ]

# 设置起始点和终点
start_grid = Grid(2, 0)
end_grid = Grid(2, 5)
# 搜索迷宫终点
result_grid = a_star_search(start_grid, end_grid)
# 回溯迷宫路径
path = []
while result_grid is not None:
    path.append(Grid(result_grid.x, result_grid.y))
    result_grid = result_grid.parent
# 输出迷宫和路径，路径用*号表示
for i in range(0, len(MAZE)):
    for j in range(0, len(MAZE[0])):
        if contain_grid(path, i, j):
            print("*, ", end='')
        else:
            print(str(MAZE[i][j]) + ", ", end='')
    print()
