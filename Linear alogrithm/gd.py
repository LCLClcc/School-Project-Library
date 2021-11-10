import numpy as np

# compute loss
def compute_error_for_line_given_points(b, w, points):
    totalError = 0
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points)) # average
# compute gradient
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += 2 * ((w_current * x) + b_current - y)
        w_gradient += 2 * x * ((w_current * x) + b_current - y)
    b_gradient = b_gradient / N
    w_gradient = w_gradient / N
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)
    return [new_b, new_w]
def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations): # num_iteration 迭代次数
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), learning_rate)
    return [b, w]
def run():
    #points = np.genfromtxt("Ldata.txt", delimiter=",")
    points = [[0, 2.000], [1, 2.500], [2, 2.900], [3, 3.147], [4, 4.515], [5, 4.903], [6, 5.365], 
              [7, 5.704], [8, 6.853], [9, 7.971], [10, 8.561], [11, 10.000], [12, 11.280], [13, 12.900]]
    points = np.array(points)
    learning_rate = 0.01
    initial_b = 0
    initial_w = 0
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b, initial_w,
                  compute_error_for_line_given_points(initial_b, initial_w, points)))
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations at b = {1}, w = {2}, error = {3}"
          .format(num_iterations, b, w,
                  compute_error_for_line_given_points(b, w, points)))
    print(w*14+b)
    X = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
    X_p = np.array([X])
    Y = [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704, 6.853, 7.971, 8.561, 10.000, 11.280, 12.900]
    Y_p = np.array(Y)
    plt.title('GD')
    plt.xlabel('years')
    plt.ylabel('prices')
    plt.scatter(X_p[0], Y_p, c='#FF0000')
    print(X_p[0])
    plt.plot(X_p[0], (X_p[0]-2000)*w+b)
    plt.show()
run()
