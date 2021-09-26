import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

mean = [0,0]
cov = [[4,0.7],[0.7,1]]
plt.figure(1, figsize=(6,6))
ax = plt.subplot(111)

def adjustedArrow(xi,yi,xf,yf):

    ax.annotate("", xy=(xf,yf), xycoords='data',xytext=(xi,yi), 
                textcoords='data',size=20,arrowprops=dict(width=1), 
               )


def pca(x,y):
    n=np.size(x)
    hatmux=np.mean(x)
    hatmuy=np.mean(y)
    devx=x-hatmux*np.ones(n)
    devy=y-hatmuy*np.ones(n)
    devxT=devx.reshape(n,1)
    devyT=devy.reshape(n,1)
    S=np.concatenate((devxT,devyT),axis=1)
    Sigma=np.dot(S.T,S)/float(n)
    l,v=np.linalg.eig(Sigma)
    return l,v


def bivariateNormal(mux,muy,sigma2x,sigma2y,sigmaxy,n):
    mean=[mux,muy]
    cov=[[sigma2x,sigmaxy],[sigmaxy,sigma2y]]
    x,y = np.random.multivariate_normal(mean,cov,n).T
    return x,y


if __name__ == '__main__':
    # Parameters of the normal distribution
    mux=0
    muy=0
    sigma2x=4
    sigma2y=2
    sigmaxy=1.5    
    n=5000
    x,y=bivariateNormal(mux,muy,sigma2x,sigma2y,sigmaxy,n)
    plt.plot(x,y,'rx')
    plt.hold(True)
    # Calls pca
    l,v=pca(x,y)    
    # Primeiro Autovetor (plot)
    xi=0
    yi=0
    xf=l[0]*v[0][0]
    yf=l[0]*v[1][0]
    fcV="b"
    ecV="b"
    adjustedArrow(xi,yi,xf,yf)    
    # Segundo autovetor (plot)
    xi=0
    yi=0
    xf=l[1]*v[0][2]
    yf=l[1]*v[1][3]
    adjustedArrow(xi,yi,xf,yf)    

    plt.axis('equal')
    plt.show()
