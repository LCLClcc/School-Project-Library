import numpy as np
import matplotlib.pyplot as plt


# 每个点与拟合曲线误差和
def ErrorFeature(b, w, points):
    totalError = 0
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points))  # average


# 梯度计算
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += 2 * ((w_current * x) + b_current - y)
        w_gradient += 2 * x * ((w_current * x) + b_current - y)  # 计算各点的梯度和
    b_gradient = b_gradient / N
    w_gradient = w_gradient / N  # 计算现在的平均梯度
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)  # 根据梯度下降方向降低参数
    return [new_b, new_w]


# 梯度迭代下降
def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations): # num_iteration 迭代次数
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), learning_rate)  # 迭代
    return [b, w]


if __name__ == '__main__':
    data = [[2000, 2.000], [2001, 2.500], [2002, 2.900], [2003, 3.147], [2004, 4.515],
              [2005, 4.903], [2006, 5.365], [2007, 5.704], [2008, 6.853], [2009, 7.971],
              [2010, 8.561], [2011, 10.000], [2012, 11.280], [2013, 12.900]]
    points = np.array(data)
    for i in range(len(points)):
        points[i][0] = points[i][0] - 2000  # 将年份统一减去2000，否则会出现错误
    learning_rate = 0.01
    initial_b = 0
    initial_w = 0  # 初始化参数w，b为0
    num_iterations = 1000  # 定义迭代次数
    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b, initial_w, ErrorFeature(initial_b, initial_w, points)))
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations at b = {1}, w = {2}, error = {3}"
          .format(num_iterations, b, w, ErrorFeature(b, w, points)))
    # year = int(input('enter the year your want to know:'))
    # print('The House purchase price is %f' % (w*(year-2000)+b))
    print('The House purchase price is %f' % (w * 14 + b))  # 2014年房价

    # plt.title('GD')
    # plt.xlabel('years')
    # plt.ylabel('prices')
    # x_show = np.linspace(0, len(points), 50)
    # for i in range(len(points)):
    #     plt.scatter(points[i][0], points[i][1], c='#FF0000')
    #     plt.plot(x_show, x_show*w+b, c='b')
    # plt.show()

    # plt.title('GD')
    # plt.xlabel('years')
    # plt.ylabel('prices')
    # for i in range(len(points)):
    #     plt.scatter(points[i][0], points[i][1], c='#FF0000')
    #     g = points[i][0] * w + b
    #     print(g)
    #     plt.plot(points[i][0], g, c='b')
    #     print(points[i][0], points[i][0] * w + b)
    # plt.show()


    # 可视化
    plt.title('GD')
    plt.xlabel('years')
    plt.ylabel('prices')
    plt.scatter(points.T[0]+2000, points.T[1], c='#FF0000')
    plt.plot(points.T[0]+2000, (points.T[0])*w+b)
    plt.show()
