#!/usr/bin/env python3
import math
import random
def optstrategy(N,k,alpha,beta):
    plans = {}
    if len(alpha) != len(beta):
        return -1
    
    
def combinations(N,k):
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
    return masterplan


print(combinations(5,5))