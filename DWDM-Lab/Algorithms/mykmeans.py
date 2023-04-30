import random

def kmeans(pts,k):
    cents=random.sample(pts,k)
    while True:
        cs=[[] for _ in range(k)]
        for pt in pts:
            dist=[((pt[0]-c[0])**2+(pt[1]-c[1])**2)**0.5 for c in cents]
            c_idx=dist.index(min(dist))
            cs[c_idx].append(pt)
        newcents=[]
        for c in cs:
            n=len(c)
            if len(c) > 0:
                c_x=[p[0] for p in c]
                c_y=[p[1] for p in c]
                newcents.append((sum(c_x)/n, sum(c_y)/n))
            else:
                newcents.append(cents[cs.index(c)])
        if newcents==cents:
            break
        else:
            cents=newcents
    return cs, cents

def get_c_cents(cs):
    cents=[]
    for c in cs:
        c_x=[p[0] for p in c]
        c_y=[p[1] for p in c]
        cent=(sum(c_x)/len(c),sum(c_y)/len(c))
        cents.append(cent)
    return cents

cs=[]
cents=[]
pts=[(1,2),(3,4),(5,6),(7,8),(9,10)]
k=2
cs, cents=kmeans(pts, k)

print(cs)
print(cents)

