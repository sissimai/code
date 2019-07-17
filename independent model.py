# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np

#set a y for example to test the code
y=[1,1,0,1,0]

#define the index functions
def index1(y):
    k=[]
    n=len(y)
    for i in range(0,n,1):
        if y[i]==0:
            k.append(1)
        else: 
            k.append(0)
    return k

def index2(y):
    l=[]
    n=len(y)
    for i in range(0,n,1):
        if y[i] == 1:
            l.append(1)
        else: 
            l.append(0)
    return l

#use index functions to help expressing the probability expression wanted
def Prob_x_given_y(p,q,x,y):
    n=len(y)
    plist= [i*(p**(sum(x)))*((1-p)**(n-sum(x))) for i in index1(y)]
    qlist= [i*(q**(sum(x)))*((1-q)**(n-sum(x))) for i in index2(y)]
    prob_i = [x+y for x,y in zip(plist,qlist)]
    Prob = np.prod(prob_i)
    return Prob

#return the values to form a list
P=[]
for p in np.arange(0,1.1,0.1):
    for q in np.arange(0,1.1,0.1):
        P.append(Prob_x_given_y(p,q,x,y))
print(P)
        
#turn the list into a matrix 
m=len(np.arange(0,1.1,0.1))
M=np.zeros(shape=(m,m))
k=0 
for i in range(m):
    for j in range(m):
        M[i][j]=P[k]
        k+=1
        
mmax=np.argmax(M)
A=np.arange(0,1.1,0.1)
pmax=A[mmax//m]
qmax=A[mmax%m-1]
print(pmax,qmax)

