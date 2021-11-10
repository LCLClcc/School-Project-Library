import numpy as np
import matplotlib.pyplot as plt

def load_data():
    X = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
    # 以列表形式读入年份数据
    X_p = np.array(X)
    # 利用np.array()函数变换数据类型为多维数组
    Y = [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704, 6.853, 7.971, 8.561, 10.000, 11.280, 12.900]
    Y_p = np.array(Y)
    return X_p, Y_p


def close_form(X, Y):
    X = np.array([X])
    one = np.ones((1, 14))
    vx = np.concatenate([one, X])
    # 假设拟合函数为一次函数，则表达式可表示为[w b][x 1].T，故构造一个2*14的矩阵
    param = np.dot(np.dot(np.linalg.inv(np.dot(vx, vx.T)), vx), Y.T)
    # 得到的矩阵为原矩阵的转置，故公式变化为（XX.T）.-1XY
    print(param)
    b = param[0]
    w = param[1]
    y = X[0] * w + b
    # 可视化
    plt.title('Close Form')
    plt.xlabel('years')
    plt.ylabel('prices')
    plt.scatter(X[0], Y, c='r')
    plt.plot(X[0], y)
    plt.show()

    print("the house purchase price in 2014 is %f"%(2014 * w + b))

if __name__ == "__main__":
    # 主函数入口语句,判断主函数用，若作为导入文件执行则不执行下面的语句
    X, Y = load_data()
    print("-----------------close form-------------------")
    close_form(X, Y)