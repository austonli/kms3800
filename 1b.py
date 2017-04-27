#!/usr/bin/env python3
import math
import random
import itertools
from scipy.stats import beta as Beta

"""iterating through all possible plans for a given N,k and finding the optimal strategy"""
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

"""iterating all possible plans using recursion"""
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
"""choosing the highest EV outcome as the EV of the plan"""
def EVplan(plan,alpha,beta):
    outcomeEVs = [0]*len(outc(plan))
    for i in range(0,len(outc(plan))):
        outcomeEVs[i] = EVoutcome(plan,outc(plan)[i],alpha,beta)
    return sum(outcomeEVs)

"""the updated EV value for a specfic outcome of a plan"""
def EVoutcome(plan,outcome,alpha,beta):
    posteriors = [0] *len(outcome)
    for k in range(0,len(outcome)):
        posteriors[k] = (alpha[k]+outcome[k])/(alpha[k]+beta[k]+plan[k]-outcome[k])
    return max(posteriors)*probout(plan,outcome,alpha,beta)


"""finding the probability of a signal sequence/outcome"""
def probout(plan,outcome,alpha,beta):
    prob = 1
    for i in range(0,len(outcome)):
        prob = prob * posterior(outcome[i],plan[i],alpha[i],beta[i])
    return prob

"""finding the probability of s successes given n trials with its corresponding alpha and beta values"""
def posterior(s,n,alpha,beta):
    combination = comb(n,s)
    betanew = betaf(alpha+s,beta+n-s)
    betaold = betaf(alpha,beta)
    return combination*betanew/betaold

"""beta function for a given a and b value"""
def betaf(a,b):
    f = math.factorial
    return (f(a-1)*f(b-1))/f(a+b-1)

"""hardcoded version of the combination function for nCr"""
def comb(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

"""a failed attempt at iterating the outcomes of a
plan using cartesian products"""
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

"""efficient way of enumerating the possible outcomes of a plan"""
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

"""for i in range(0,6):
    print(posterior(i,3,1,1))"""

#print(outc([5,5,5,5,5]))
alphas = [1]*5
betas = [1]*5
alphaother = [10]
alphaother += [1]*4
betaother = [10]
betaother += [1]*4

print(EVplan([1,2,1,1,1],alphas,betas))

#print(outc([1,1,2]))
#print(EVplan([1,1,3,2,1],alphas,betas))
#print(recurcomb(25,5))
#print(optstrategy(8,5,alphas,betas))
#print(optstrategy(25,5,alphaother,betaother))