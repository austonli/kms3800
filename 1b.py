#!/usr/bin/env python3
import math
import random
import itertools
from scipy.stats import beta as Beta
def optstrategy(N,k,alpha,beta):
    allplans = recurcomb(N,k)
    EVarray = [0]*len(allplans)
    for z in range(0,len(allplans)):
        EVarray[z] = EVplan(allplans[z],alpha,beta)
    return max(EVarray),allplans[EVarray.index(max(EVarray))]
    
    
"""def combinations(N,k):
    maxlength =  int(math.factorial(N+k-1)/(math.factorial(N)*math.factorial(k-1)))
    plan = [0]*k
    masterplan = []
    currentlength = 0
    while (currentlength < maxlength):
        currentlength = len(masterplan)
        plan = [0]*k
        for i in range(0,k):
            x = random.randint(0,N)
            if (sum(plan) < N and sum(plan) + x <= N):
                plan[i] = x
        if (plan not in masterplan and sum(plan) == N):
            masterplan.append(plan)
    return masterplan"""


def recurcomb(N,k):
    if (k == 1):
        return [N]
    masterplan = []
    for x in range(0,N+1):
        if (k == 2):
            step = recurcomb(N-x,k-1)
            step.insert(0,x)
            masterplan.append(step)
        else:
            step = recurcomb(N-x,k-1)
            for z in range (0,len(step)):
                step[z].insert(0,x)
            masterplan += step
        
    return masterplan

def EVplan(plan,alpha,beta):
    outcomeEVs = [0]*len(outcomes(plan))
    for i in range(0,len(outcomes(plan))):
        outcomeEVs[i] = EVoutcome(plan,outcomes(plan)[i],alpha,beta)
    return max(outcomeEVs)


def EVoutcome(plan,outcome,alpha,beta):
    prob = 1
    for i in range(0,len(outcome)):
        prob = prob * posterior(outcome[i],plan[i],alpha[i],beta[i])
    posteriors = [0] *len(outcome)
    for k in range(0,len(outcome)):
        posteriors[k] = (alpha[k]+outcome[k])/(alpha[k]+beta[k]+plan[k]-outcome[k])
    print(max(posteriors)*prob)
    return max(posteriors)*prob

def posterior(s,n,alpha,beta):
    combination = comb(n,s)
    betanew = betaf(alpha+s,beta+n-s)
    betaold = betaf(alpha,beta)
    return combination*betanew/betaold


def betaf(a,b):
    f = math.factorial
    return (f(a-1)*f(b-1))/f(a+b-1)

def comb(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def outcomes(plan):
    #sum of indices must be <= sum(plan)
    #each index of outcome is <= index of plan
    productset=[]
    maxsum = sum(plan)
    indexset =[]
    print("done")
    for z in range(0,maxsum+1):
        indexset += [z]
    for i in itertools.product(indexset,repeat=len(plan)):
        productset.append(list(i))
    filterset =[]
    print("done")
    for z in productset:
        for j in range(0,len(z)):
            if z[j]> plan[j]:
                filterset.append(z)
    filtered = []
    print("done")
    for m in productset:
        if m not in filterset:
            print(m)
            filtered.append(m)
    twofilter = []
    print("done")
    for k in filtered:
        if sum(k) <= maxsum:
            twofilter.append(k)
    return twofilter


def outc(plan):
    lists = []
    zeroz = [0]*len(plan)
    while zeroz[0] <= plan[0]:
        lists.append(list(zeroz))
        zeroz[-1] +=1
        for i in range(len(plan)-1,0,-1):
            if zeroz[i] > plan[i]:
                zeroz[i] =0
                zeroz[i-1] += 1
        

    return lists




print(outc([1,2,5,1,1]))
alphas = [1]*5
betas = [1]*5
alphaother = [10]
alphaother += [1]*4
betaother = [10]
betaother += [1]*4
#print(recurcomb(25,5))
#print(optstrategy(6,2,alphas,betas))
#print(optstrategy(25,5,alphaother,betaother))