# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:49 2021

@author: aniss
"""
import matplotlib.pyplot as plt

def trianglePascal(n):
    T = [[0] * (n+1) for p in range(n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[n][0] = 1
                else:
                    T[n][k] = T[n-1][k-1] + T[n-1][k]
    return T

def Bn(u,T,n,i):
    return T*(u**i)*((1-u)**(n-i-1))
    #(n-i-1) : le -1 car on a n points de contrôle
    

def bezier(liste_P,epsilon):
    liste_x=[]
    liste_y=[]
    n=len(liste_P)
    #on a n points de contrôle 
    u=0
    
    triangle = trianglePascal(n)
    
    while(u<1):
        px=0
        py=0
        
        for i in range(n):
            B=Bn(u,triangle[n-1][i],n,i)
            px += B*liste_P[i][0]
            py += B*liste_P[i][1]
            
        liste_x.append(px)
        liste_y.append(py)
        
        u+=epsilon
    
    
    
    return liste_x,liste_y

#polygone_control = [[0,0],[4,4],[8,0]]
polygone_control = [[0,0],[0,4],[8,4],[8,0]]
res = bezier(polygone_control,0.1)

plt.plot([x for [x,y] in polygone_control],[y for [x,y] in polygone_control],"r-")
plt.plot(res[0],res[1],"b-")

#Pour une courbe complexe avec des boucles et 16 points
plt.figure(2)
p = [[2,0],[0,1],[1,4],[4,2],[8,-1],[12,-4],[17,-1],[20,1],[14,5],[8,-5],[6,-8],[13,-13],[15,-11],[17,-9],[14,-7],[12,-9]]
res2 = bezier(p,0.01)
plt.plot([x for [x,y] in p],[y for [x,y] in p],"r-")
plt.plot(res2[0],res2[1],"b-")

#Test complexe par morceau avec 16 points
p0 = [[2,0],[0,1],[1,4],[4,2]]
p1 = [[4,2],[8,-1],[12,-4],[17,-1]]
p2 = [[17,-1],[20,1],[14,5],[8,-5]]
p3 = [[8,-5],[6,-8],[13,-13],[15,-11]]
p4 = [[15,-11],[17,-9],[14,-7],[12,-9]]

liste= []
liste.append(p0)
liste.append(p1)
liste.append(p2)
liste.append(p3)
liste.append(p4)


plt.figure(3)
for i in range (5):
    res3 = bezier(liste[i],0.01)
    plt.plot([x for [x,y] in liste[i]],[y for [x,y] in liste[i]],"r-")
    plt.plot(res3[0],res3[1],"b-")
plt.show()

#------------------------------------------------------------------------------
#Figure 1
pFigure1=[[0,0],[3,9],[6,9],[9,4],[12,4],[15,9],[18,9],[21,0]]
plt.figure(4)
res=bezier(pFigure1,0.01)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res[0],res[1],"b-")

#Figure 2
pFigure2=[[1,0],[0,3],[1,5],[3,2],[4,1],[5,3],[4,4],[5,7],[7,4],[6,1],[9,1],[9,4],[7,9],[3,9],[2,7]]
plt.figure(5)
res=bezier(pFigure2,0.01)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res[0],res[1],"b-")

#Figure 3
pFigure3=[[4,1],[0,3],[1,8],[5,9],[8,8],[6,3],[4,1]]
plt.figure(6)
res=bezier(pFigure3,0.01)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res[0],res[1],"b-")
