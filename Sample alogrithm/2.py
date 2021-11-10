import numpy as np

'''
类:Point
用来标识坐标点
'''


class Point(object):
    def __init__(self, x, y):
        self.row = x
        self.col = y


'''
函数：判断两个点是否相同
参数:
    Point p1 
    Point p2
'''


def isSamePoint(p1, p2):
    if (p1.row == p2.row) and (p1.col == p2.col):
        return True
    else:
        return False


'''
函数：获取相邻未被访问的节点(上下左右)
参数说明：
    mark：节点标记
    point：节点 
    m：行 
    n：列
'''


def getAdjacentNotVisitedNode(mark, point, m, n):
    resP = Point(-1, -1)
    if (point.row - 1 >= 0) and (mark[point.row - 1][point.col] == 0):
        resP.row = point.row - 1
        resP.col = point.col
        return resP

    if (point.col + 1 < n) and (mark[point.row][point.col + 1] == 0):
        resP.row = point.row
        resP.col = point.col + 1
        return resP

    if (point.row + 1 < m) and (mark[point.row + 1][point.col] == 0):
        resP.row = point.row + 1
        resP.col = point.col
        return resP

    if (point.col - 1 >= 0) and (mark[point.row][point.col - 1] == 0):
        resP.row = point.row
        resP.col = point.col - 1
        return resP
    return resP


'''
函数：寻路函数
参数：
    maze：地图
    m：行 
    n：列
    pointStack：点栈，用于存放路径
'''


def mazePath(maze, m, n, startP, endP, pointStack):
    if (maze[startP.row][startP.col] == 1) or (maze[endP.row][endP.col] == 1):
        return
        #
    mark = maze

    # 将起点入栈
    pointStack.append(startP)
    mark[startP.row][startP.col] = 0

    # 栈不空并且栈顶元素不为结束节点
    ptop = pointStack[-1]

    while (len(pointStack) != 0) and (isSamePoint(ptop, endP) == False):
        ptop = pointStack[-1]
        adjacentNotVisitedNode = getAdjacentNotVisitedNode(mark, ptop, m, n)
        if adjacentNotVisitedNode.row == -1:
            pointStack.pop()
            continue
        mark[adjacentNotVisitedNode.row][adjacentNotVisitedNode.col] = 1
        pointStack.append(adjacentNotVisitedNode)


def main():
    # 地图：0是可走的地方，1是障碍物
    maze = np.array([
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0]
    ])

    startP = Point(0, 0)  # 起点坐标
    endP = Point(4, 4)  # 终点坐标

    pointStack = []  # 设置点栈
    mazePath(maze, 5, 5, startP, endP, pointStack)  # 执行寻路函数

    if len(pointStack) == 0:
        print('Died.....No way can go')
    else:
        tmpStack = []
        print('Path:')
        while len(pointStack) > 0:
            tmpStack.append(pointStack[-1])
            pointStack.pop()
        while len(tmpStack) > 0:
            p = tmpStack.pop()
            print('<{},{}>'.format(p.row, p.col))


if __name__ == "__main__":
    main()
