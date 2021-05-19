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
listeControle=[[0,0],[0,5],[5,5],[5,0]]

def BSpline(liste_P,epsilon,k,n,U):
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

#-------------------------------------------------------------
k=3
n=3
U=vectUniforme(k, n)

res = BSpline(listeControle,0.01,k,n,U)
plt.plot([x for [x,y] in listeControle],[y for [x,y] in listeControle],"r-")
plt.plot(res[0],res[1],"b-")

#-------------------------------------------------------------
pBezier = [[2,0],[0,1],[1,4],[4,2],[8,-1],[12,-4],[17,-1],[20,1],[14,5],[8,-5],[6,-8],[13,-13],[15,-11],[17,-9],[14,-7],[12,-9]]
n2=15
#Pour vecteur uniforme et k=2
k2=2
U2=vectUniforme(k2, n2)
plt.figure(2)
res2 = BSpline(pBezier,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pBezier],[y for [x,y] in pBezier],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniforme(k2, n2)
plt.figure(3)
res2 = BSpline(pBezier,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pBezier],[y for [x,y] in pBezier],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniforme(k2, n2)
plt.figure(4)
res2 = BSpline(pBezier,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pBezier],[y for [x,y] in pBezier],"r-")
plt.plot(res2[0],res2[1],"b-")

#-------------------------------------------------------------
#Pour vecteur ouvert uniforme et k=2
k2=2
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(5)
res2 = BSpline(pBezier,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pBezier],[y for [x,y] in pBezier],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(6)
res2 = BSpline(pBezier,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pBezier],[y for [x,y] in pBezier],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(7)
res2 = BSpline(pBezier,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pBezier],[y for [x,y] in pBezier],"r-")
plt.plot(res2[0],res2[1],"b-")


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
pFigure1=[[0,0],[3,9],[6,9],[9,4],[12,4],[15,9],[18,9],[21,0]]
n2=7
#Pour vecteur uniforme et k=2
k2=2
U2=vectUniforme(k2, n2)
plt.figure(8)
res2 = BSpline(pFigure1,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniforme(k2, n2)
plt.figure(9)
res2 = BSpline(pFigure1,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniforme(k2, n2)
plt.figure(10)
res2 = BSpline(pFigure1,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res2[0],res2[1],"b-")

#-------------------------------------------------------------
#Pour vecteur ouvert uniforme et k=2
k2=2
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(11)
res2 = BSpline(pFigure1,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(12)
res2 = BSpline(pFigure1,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(13)
res2 = BSpline(pFigure1,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure1],[y for [x,y] in pFigure1],"r-")
plt.plot(res2[0],res2[1],"b-")


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
pFigure2=[[1,0],[0,3],[1,5],[3,2],[4,1],[5,3],[4,4],[5,7],[7,4],[6,1],[9,1],[9,4],[7,9],[3,9],[2,7]]
n2=14
#Pour vecteur uniforme et k=2
k2=2
U2=vectUniforme(k2, n2)
plt.figure(14)
res2 = BSpline(pFigure2,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniforme(k2, n2)
plt.figure(15)
res2 = BSpline(pFigure2,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniforme(k2, n2)
plt.figure(16)
res2 = BSpline(pFigure2,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res2[0],res2[1],"b-")

#-------------------------------------------------------------
#Pour vecteur ouvert uniforme et k=2
k2=2
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(17)
res2 = BSpline(pFigure2,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(18)
res2 = BSpline(pFigure2,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(19)
res2 = BSpline(pFigure2,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure2],[y for [x,y] in pFigure2],"r-")
plt.plot(res2[0],res2[1],"b-")

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
pFigure3=[[4,1],[0,3],[1,8],[5,9],[8,8],[6,3],[4,1]]
n2=6
#Pour vecteur uniforme et k=2
k2=2
U2=vectUniforme(k2, n2)
plt.figure(20)
res2 = BSpline(pFigure3,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniforme(k2, n2)
plt.figure(21)
res2 = BSpline(pFigure3,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniforme(k2, n2)
plt.figure(22)
res2 = BSpline(pFigure3,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res2[0],res2[1],"b-")

#-------------------------------------------------------------
#Pour vecteur ouvert uniforme et k=2
k2=2
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(23)
res2 = BSpline(pFigure3,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=3
k2=3
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(24)
res2 = BSpline(pFigure3,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res2[0],res2[1],"b-")

#Pour vecteur uniforme et k=4
k2=4
U2=vectUniformeOuvert(k2, n2, 0)
plt.figure(25)
res2 = BSpline(pFigure3,0.01,k2,n2,U2)
plt.plot([x for [x,y] in pFigure3],[y for [x,y] in pFigure3],"r-")
plt.plot(res2[0],res2[1],"b-")
