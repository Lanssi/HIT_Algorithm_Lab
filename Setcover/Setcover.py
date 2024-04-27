import random
import copy
import pulp

'''
Configuration
'''
size = 100

#Note: This generation method is not so good
def generate_data(size):
    S = {i for i in range (1, size+1)}
    R = copy.deepcopy(S)
    F = []
    for i in range(size):
        if R:
            num = random.randint(1, len(R)//2+1)
            subset = set(random.sample(list(R), num))
            F.append(subset)
            R -= subset
        else:
            num = random.randint(1, size//2+1)
            subset = set(random.sample(list(S), num))
            F.append(subset)

    return S, F

def greedy(S, F):
    S_copy = copy.deepcopy(S)
    F_copy = copy.deepcopy(F)
    M = [] #which means the minimum

    while S_copy:
        #select the best subset in F
        best = None
        max_cover = 0
        for subset in F_copy:
            cover = len(S_copy & subset)
            if cover > max_cover:
                max_cover = cover
                best = subset

        S_copy -= best
        F_copy.remove(best)
        M.append(best)

    return M

def LP(S, F):
    #calculate the frequency for lateral rounding
    frequency = [0]*len(S)
    for subset in F:
        for elem in subset:
            frequency[elem-1] += 1
    theta = 1/max(frequency)
    #theta = 1/size

    #create a LP problem
    prob = pulp.LpProblem("Setcover", pulp.LpMinimize)
    
    #create variables
    x = pulp.LpVariable.dicts("Set", range(len(F)), lowBound=0, upBound=1, cat='Continuous')

    #define objective function
    prob += pulp.lpSum([x[i] for i in range(len(F))])

    #define constraint
    for elem in S:
        prob += pulp.lpSum([x[i] for i in range(len(F)) if elem in F[i]]) >= 1

    #solve the problem
    prob.solve()

    M = []
    for i in range(len(F)):
        if x[i].varValue >= theta:
            M.append(F[i])

    return M
    

def check(S, M):
    merge_set = set()
    for subset in M:
        merge_set |= subset
    return S == merge_set

'''
Main function
'''
if __name__ == '__main__':
    random.seed()
    S, F = generate_data(size)
    M = LP(S, F)
    print(len(F))
    print(len(M))
    print(check(S, M))
