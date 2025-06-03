import numpy as np
A = [0, 0, 1, 1]
B = [0, 1, 0, 1]
D_n = [0, 0, 0, 1]
w_1 = 0.9
w_2 = 0.9
x_0 = 1
w_0 = 0
learning_rate = 0.5
thres = 0.5
n = 5

def activation_function(o):
    if(o>thres):
        return 1
    else:
        return 0

for i in range(n):
    print("Iteration: ",i+1)
    for j,k,l in zip(A,B,D_n):
        o = w_1*j + w_2*k + x_0*w_0
        h = activation_function(o)
        print("The predicted value is: ",h)
        print("The actual value: ",l)
        if(h == l):
            continue
        else:
            w_1 = w_1 + learning_rate*(l-h)*j
            w_2 = w_2 + learning_rate*(l-h)*k
            w_0 = w_0 + learning_rate*(l-h)*x_0
    print("---------------")
print("Final weight_1", w_1)
print("Final_weight 2",w_2)
print("Final_bias",w_0)
