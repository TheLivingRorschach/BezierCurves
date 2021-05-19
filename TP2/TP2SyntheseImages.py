# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:32:44 2021

@author: aniss
"""
import matplotlib.pyplot as plt
#Les vecteurs uniformes et uniformes ouverts reprèsentent U de taille k+n+1
def vectUniforme(k,n):
    vect=[]
    for x in range(k+n+1):
        vect.append(x)
    return vect

def vectUniformeOuvert(k,n,debut):
    vect=[]
    for x in range(k):
        vect.append(debut)
    for x in range(n+1-k):
        debut+=1
        vect.append(debut)
    for x in range(k):
        vect.append(debut+1)
    return vect

# u est dans l'interval [U[k-1], U[n+1]]
liste_P=[[0,0],[3,3],[6,3],[9,0],[12,0],[15,3],[18,3],[21,0],[24,0],[27,3],[30,3],[33,0]]
listeControle=[[0,0],[0,16],[16,16],[16,0]]

def BSpline(liste_P,epsilon):
    k=3
    n=3 #nombre de points de controle -1
    U=[x for x in range(k+n+1)]
    u=U[k-1]
    
    liste_x=[]
    liste_y=[]
    
    
    while(u<=U[n+1]):
        i=k
        dec=0
        while(u>U[i]):
            dec+=1
            i=i+1
        cop=[]
        for x in liste_P:
            cop.append([x[0],x[1]])
        listebis=[cop[dec+x] for x in range(k)]
        
        for j in range(k-1):
            for i in range(k-1-j):
                listebis[i][0]=(U[dec+k+i]-u)/(U[dec+k+i]-U[dec+1+i+j])*listebis[i][0] + (u-U[dec+1+i+j])/(U[dec+k+i]-U[dec+1+i+j])*listebis[i+1][0]
                listebis[i][1]=(U[dec+k+i]-u)/(U[dec+k+i]-U[dec+1+i+j])*listebis[i][1] + (u-U[dec+1+i+j])/(U[dec+k+i]-U[dec+1+i+j])*listebis[i+1][1]
        liste_x.append(listebis[0][0])
        liste_y.append(listebis[0][1])
        u+=epsilon
    
    return liste_x,liste_y

res = BSpline(listeControle,0.01)
plt.plot([x for [x,y] in listeControle],[y for [x,y] in listeControle],"r-")
plt.plot(res[0],res[1],"b-")

a=vectUniformeOuvert(3, 5, 0)
print(a)
