import itertools, random, math
import numpy as np
from scipy.optimize import differential_evolution, minimize


def prob(weights,p):
    n=len(weights)
    ans=0.0
    for mask in range(1<<n):
        s=0.0; k=0
        for i,w in enumerate(weights):
            if mask>>i &1:
                s+=w; k+=1
        if s+1e-12>=p:
            ans += (p**k)*((1-p)**(n-k))
    return ans

def softmax(y):
    e=np.exp(y-np.max(y)); return e/e.sum()

def obj(y,p,n):
    w=softmax(np.array(y))
    return prob(w,p)

for p in [0.05,0.1,0.2,0.3,1/3,0.34,0.4]:
    print('p',p)
    for n in range(1,9):
        best=1
        bestw=None
        # differential evolution over logits bounded
        res=differential_evolution(lambda y: obj(y,p,n), [(-8,8)]*n, tol=1e-8, polish=True, workers=1, maxiter=400, popsize=10, seed=123+n)
        best=res.fun; bestw=softmax(res.x)
        print(n, best, 'gap', best-p, 'w', np.round(np.sort(bestw)[::-1],4))
    print()
