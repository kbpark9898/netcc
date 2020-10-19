import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

def cluster(cord_x, cord_y):        
    #가우시안분포 활용한 랜덤 좌표 생성
    #나머지 두개의 좌표를 조절할것
    g0=np.random.multivariate_normal([cord_x, cord_y], [[0.0005,0],[0,0.0005]], 100)
    g1=np.random.multivariate_normal(["lat,lon"], [[0.0005,0],[0,0.0005]], 100)
    g2=np.random.multivariate_normal(["lat, lon"], [[0.0005,0],[0,0.0005]], 100)
    # g0=np.random.rand(100, 2)
    # g1=np.random.rand(100, 2)
    # g2=np.random.rand(100,2)
    x=np.vstack([g0, g1, g2])
    x=np.asmatrix(x)
    print(x)
  
    k=3
    m=x.shape[0]

    mu = x[np.random.randint(0, m, k), :]
    pre_mu = copy.deepcopy(mu)
    print(mu)
  
    samecount = 0
    y = np.empty([m,1])
    for j in range(100):    
        for i in range(m):
            d0=np.linalg.norm(x[i,:]-mu[0,:],2)
            d1=np.linalg.norm(x[i,:]-mu[1,:],2)
            d2=np.linalg.norm(x[i,:]-mu[2,:],2)
            y[i]=np.argmin([d0, d1, d2])
        for i in range(k):
            mu[i, :] = np.mean(x[np.where(y==i)[0]], axis = 0)
        print("current step is... ", j)
        print(mu)
        # if (pre_mu == mu).all():
        #     samecount+=1
        #     pre_mu = copy.deepcopy(mu)
        # if samecount>10:
        #     break



    x0 = x[np.where(y==0)[0]]
    x1=x[np.where(y==1)[0]]
    x2=x[np.where(y==2)[0]]
  

    print(mu)
    final_x = 0
    final_y =0
    for i in mu:
        final_x += i[:, 0]
        final_y += i[:, 1]

    print(final_x[0]/3, final_y[0]/3)
    return [final_x[0]/3, final_y[0]/3]
 