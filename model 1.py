# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

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

p = np.arange(0,1.1,0.1)
q = np.arange(0,1.1,0.1)
x=[0,0,1,0,1]
y=[1,1,0,1,0]


def max_pq(p,q):
    m=len(p)
    P = np.zeros(shape=(m,m))
    for i in range(m):
        for j in range(m):
            P[i][j]= Prob_x_given_y(p[i],q[j],x,y)
    maxprob = np.where(P == np.amax(P))
  
    #more accurate
    p= np.arange(maxprob[0]-0.1,maxprob[0]+0.11,0.01)
    q= np.arange(maxprob[1]-0.1,maxprob[1]+0.11,0.01)
    m=len(p)
    Q = np.zeros(shape=(m,m))
    for i in range(m):
        for j in range(m):
            Q[i][j]= Prob_x_given_y(p[i],q[j],x,y)
    maxprob = np.where(Q == np.amax(Q))
    
    listOfCordinates = list(zip(maxprob[0], maxprob[1]))
    for cord in listOfCordinates:
        print(cord)
  

    
