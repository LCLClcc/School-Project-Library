import sys
import time
import matplotlib.pyplot as plt


from matplotlib.patches import Rectangle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = -1
        # 代价
        self.cost = 0

    def __str__(self):
        return "Point(%s,%s),parent=%s" % (self.x, self.y, self.parent)

    def __repr__(self):
        return self.__str__()


class Map:

    def __init__(self, size=36):
        # 定义地图的尺寸
        self.size = size
        # 定义障碍物的点
        self.obstacle_points = []
        # 生成障碍物
        self.generate_obstacle()

    def generate_obstacle(self):
        print("生成障碍物...")

        # 左边的墙
        for i in range(self.size):
            self.obstacle_points.append(Point(i, 0))

        # 右边的墙
        for i in range(self.size):
            self.obstacle_points.append(Point(i, self.size - 1))

        # 上边的墙
        for i in range(self.size):
            self.obstacle_points.append(Point(0, i))

        # 下边的墙
        for i in range(self.size):
            self.obstacle_points.append(Point(self.size - 1, i))

        # 左边的障碍物
        for y in range(self.size):
            if y <= 18 or y >= 30:
                self.obstacle_points.append(Point(9, y))

        # 中间的障碍物
        for y in range(9, 27):
            self.obstacle_points.append(Point(18, y))

        # 右边的障碍物
        for y in range(self.size):
            if y <= 6 or y >= 30 or (y >= 15 and y <= 21):
                self.obstacle_points.append(Point(27, y))

    def IsObstacle(self, i, j):
        """判断是否是障碍物"""
        # print(self.obstacle_points)
        for p in self.obstacle_points:
            if i == p.x and j == p.y:
                return True
        return False


class AStar:
    def __init__(self, map):
        # 寻路地图
        self.map = map
        # 待遍历的点
        self.open_set = []
        # 已经遍历的节点
        self.close_set = []

    # 计算距离起点的距离
    def BaseCost(self, p, father):
        # print('计算BaseCost ： [', p.x, ',', p.y, ']', ', [', father.x, ',', father.y, ']')

        if (abs(p.x - father.x) == 1 and abs(p.y - father.y) == 1):
            G = father.cost + 14
        else:
            G = father.cost + 10
        return G
        # x_dis = abs(p.x - self.startPoint.x)
        # y_dis = abs(p.y - self.startPoint.y)
        # # Distance to start point
        # return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    # # 计算距离终点的曼哈顿距离
    # def HeuristicCost(self, p):
    #     x_dis = abs(self.endPoint.x - p.x)
    #     y_dis = abs(self.endPoint.y - p.y)
    #     # Distance to end point
    #     # return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)
    #     return (x_dis + y_dis) * 10

    # 总的代价
    def TotalCost(self, p, father):
        # print('basecost:', self.BaseCost(p, father), '   H cost:', self.HeuristicCost(p), ' ', p.x, ' ', p.y, ' ', father.x, ' ', father.y)
        return self.BaseCost(p, father)

    def IsValidPoint(self, x, y):
        # 判断是否超过地图边界
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        # 是否不是障碍物
        return not self.map.IsObstacle(x, y)

    # 判断点是否在列表中
    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    # 判断是否在 open 列表中
    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    # 判断是否在 close 列表中
    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    # 找出 open 列表中 p 的下标
    def GetOpenList(self, p):
        for index, point in enumerate(self.open_set):
            if point.x == p.x and point.y == p.y:
                return index
        return False

    # 是否是起点
    def IsStartPoint(self, p):
        return p.x == self.startPoint.x and p.y == self.startPoint.y

    # 是否是终点
    def IsEndPoint(self, p):
        return p.x == self.endPoint.x and p.y == self.endPoint.y

    # # 判断是否已经遍历所有点
    # def IsEndPoint(self, p):
    #     # 判断是否超过地图边界
    #     if p.x < 0 or p.y < 0:
    #         return True
    #     if p.x >= self.map.size or p.y >= self.map.size:
    #         return True
    #     return False

    # 处理某一个点
    def ProcessPoint(self, x, y, parent):
        # 若点是无效的点，则直接跳过
        if not self.IsValidPoint(x, y):
            return  # Do nothing for invalid point

        # 判断点是否已经处理过了
        p = Point(x, y)
        if self.IsInCloseList(p):
            return  # Do nothing for visited point

        if self.IsInOpenList(p):
            index = self.GetOpenList(p)
            if self.open_set[index].cost > self.TotalCost(p, parent):
                self.open_set[index].cost = self.TotalCost(p, parent)
                self.open_set[index].parent = parent
                # print('更新计算点： [', p.x, ',', p.y, ']', ', cost: ', self.open_set[index].cost)

        # 若点不在待处理的点里面
        if not self.IsInOpenList(p):
            father = parent
            p.parent = parent
            p.cost = self.TotalCost(p, father)
            self.open_set.append(p)

            # print('新增计算点： [', p.x, ',', p.y, ']', ', cost: ', p.cost)

            rec = Rectangle((p.x, p.y), width=1, height=1, facecolor='pink')
            ax.add_patch(rec)
            plt.pause(0.000000001)

    def SelectPointInOpenList(self):
        """
            找出代价最小的点
        """
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            # cost = self.TotalCost(p)
            cost = p.cost
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p, ax, plt, start_time):
        path = []
        # 根据parent反向将所有的点添加到路径中
        while True:
            # 始终将点插到队列的前面
            path.insert(0, p)
            if self.IsStartPoint(p):
                break

            else:
                p = p.parent

        # 找到的路径绘制出来
        for p in path:
            rec = Rectangle((p.x, p.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()

        end_time = time.time()
        print('算法执行完成，耗时：', int(end_time - start_time), ' 秒')

    # A* 算法的核心逻辑
    def run(self, ax, plt, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        # 2. 将起点放入open_set，并设置代价为最高代价0
        self.startPoint.cost = 0
        self.open_set.append(self.startPoint)
        start_time = time.time()
        # 循环处理每一个点
        while True:
            # 选择移动代价最小的点出来
            index = self.SelectPointInOpenList()
            # 判断是否找到点
            if index == -1:
                print("没有找到路径")
                break

            # 取出点的信息
            p = self.open_set[index]
            # 为了便于观察当前处理到了哪个点，显示小方块
            '''
            rec = Rectangle((p.x, p.y), width=1, height=1, facecolor='pink')
            ax.add_patch(rec)
            plt.pause(0.000000001)
            '''

            # 判断点是否是终点
            if self.IsEndPoint(p):
                print("已经到达终点")
                return self.BuildPath(p, ax, plt, start_time)

            # 从待处理的点集合中删除
            del self.open_set[index]
            # 保存到已经处理的集合中
            self.close_set.append(p)

            x = p.x
            y = p.y
            # 处理8邻域所有的点
            # 上面3个邻域点
            self.ProcessPoint(x - 1, y - 1, p)
            self.ProcessPoint(x, y - 1, p)
            self.ProcessPoint(x + 1, y - 1, p)

            # 左右两个邻域
            self.ProcessPoint(x - 1, y, p)
            self.ProcessPoint(x + 1, y, p)

            # 下面3个邻域点
            self.ProcessPoint(x - 1, y + 1, p)
            self.ProcessPoint(x, y + 1, p)
            self.ProcessPoint(x + 1, y + 1, p)

# 主函数
if __name__ == '__main__':
    # 可视化
    plt.ion()
    plt.figure(figsize=(5, 5))

    # 生成地图上的点
    map = Map()

    # 初始化
    ax = plt.gca()
    ax.set_xlim([0, map.size])
    ax.set_ylim([0, map.size])

    # 将地图中的点用matplotlib绘制出来
    # 每个点用一个小方块表示
    for i in range(map.size):
        for j in range(map.size):
            if map.IsObstacle(i, j):
                rec = Rectangle((i, j), width=1, height=1, color='gray')
                ax.add_patch(rec)
            else:
                rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
                ax.add_patch(rec)

    # 定义起始点的坐标
    startPoint = Point(1, 1)
    # 定义终点的坐标
    endPoint = Point(map.size - 2, map.size - 2)

    # 左下角的起始点
    rec = Rectangle((startPoint.x, startPoint.y), width=1, height=1, facecolor='b')
    ax.add_patch(rec)

    # 右上角的目标点
    rec = Rectangle((endPoint.x, endPoint.y), width=1, height=1, facecolor='r')
    ax.add_patch(rec)

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    # 将地图数据丢给A*算法
    a_star = AStar(map)
    a_star.run(ax, plt, startPoint, endPoint)
    plt.pause(10)
    plt.close()

