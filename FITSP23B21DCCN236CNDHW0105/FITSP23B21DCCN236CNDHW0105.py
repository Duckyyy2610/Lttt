#Đặng Minh Đức
# B21DCCN236
# Lý thuyết thông tin
# Nhóm G05
# Bài 5


import matplotlib.pyplot as plt
import numpy as np
import math

def hamming_bound(n, k):
    x = np.arange(k, n + 1)
    y = np.zeros(n - k + 1)
    for i in range(k, n + 1):
        y[i - k] = sum([np.math.comb(i, j) for j in range(k)])
    return x, y
def plotkin_bound(n, k):
    x = np.arange(k, n + 1)
    y = np.zeros(n - k + 1)
    for i in range(k, n + 1):
        y[i - k] = 2 ** k / sum([i ** j for j in range(k)])
    return x, y

def Greismer_bound(d, n):
    k = 1
    while True:
        s = 0
        for i in range(d-1):
            s += math.ceil(k/2**i)
        if s <= n-d+1:
            k += 1
        else:
            return k-1


d_values = range(2, 21)
n_values = range(2, 100)
bound_values = [[Greismer_bound(d, n) for n in n_values] for d in d_values]

plt.figure(figsize=(8, 6))
for i, d in enumerate(d_values):
    plt.plot(n_values, bound_values[i], label=f'd={d}')
plt.xlabel('n')
plt.ylabel('k')
plt.title('Greismer Bound')
plt.legend()
plt.show()

n = 15
k = 5
x, y = plotkin_bound(n, k)

plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('k')
plt.title('Plotkin Bound')
plt.show()

n = 15
k = 5
x, y = hamming_bound(n, k)

plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('k')
plt.title('Hamming Bound')
plt.show()

