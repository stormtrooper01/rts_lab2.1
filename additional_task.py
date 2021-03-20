import matplotlib.pyplot as plt
import random
import math
from timeit import default_timer as timer
from datetime import timedelta

n = 10
omegaMax = 1200
N = 64

k = 128
tau = 64

def Plot(g):
    A = []
    fi = []
    for i in range(n):
        A.append(random.random())
        fii = random.random() * omegaMax
        fi.append(fii)
    for i in range(k):
        res = 0
        for j in range(n):
            res += A[j] * math.sin((omegaMax / (j + 1)) * i + fi[j])
        g.append(res)
        yy = i

start = timer()
def FourierList(g, containerType="list"):
    Fp = []
    W = []
    Re = []
    Im = []
    for i in range(N):
        Re.append(math.sin(i * 2 * math.pi / 4))
        Im.append(math.cos(i * 2 * math.pi / 4))
        W.append(math.sqrt((Re[i] * Re[i]) + (Im[i] * Im[i])))
    for k in range(N - 1):
        Wpk = 0
        for p in range(N - 1):
            Wpk = Wpk + W[(p * k) % N]
        Fp.append(g[k] * Wpk)
    return Fp
end = timer()

startF = timer()
def FourierArray(g, containerType="array"):
    Fp = []
    W = []
    Re = []
    Im = []
    for i in range(N):
        Re.append(math.sin(i * 2 * math.pi / 4))
        Im.append(math.cos(i * 2 * math.pi / 4))
        W.append(math.sqrt((Re[i] * Re[i]) + (Im[i] * Im[i])))
    for k in range(N - 1):
        Wpk = 0
        for p in range(N - 1):
            Wpk = Wpk + W[(p * k) % N]
        Fp.append(g[k] * Wpk)
    return Fp
endF = timer()

print("DFT time for list:", timedelta(end - start))
print("DFT time for array:", timedelta(endF - startF))
