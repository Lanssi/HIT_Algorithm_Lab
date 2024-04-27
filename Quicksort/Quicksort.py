import random
import pickle
from time import perf_counter

'''
Configuration
'''
size = 10**6
num_list = 11

def generate_lists(size=10**6, num_list=11):
    lists = []

    for i in range(num_list):
        repeat = int(size * 10 * i / 100)

        if repeat == 0:
            uni_list = [random.randint(0, 10000) for i in range(size)]
        elif repeat == size:
            uni_lists = [1]*size
        else:
            uni_list = [random.randint(0, 10000) for i in range(size-repeat)]
            for i in range (repeat):
                #randomly pick one element in the non_repeat array
                index = random.randint(0, size-repeat-1)
                data = uni_list[index]
                uni_list.append(data)

        random.shuffle(uni_list)
        lists.append(uni_list)

    return lists

        
def quicksort(A, p, r):
    if p < r:
        q = rand_partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def rand_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    chosen = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= chosen:
            i += 1
            A[i], A[j] = A[j], A[i]

    i+=1
    A[i], A[r] = A[r], A[i] 
    return i

'''
Main function
'''
if __name__ == '__main__':
    data_path = "./lists.pkl"
    
    #lists = generate_lists(size, num_list)
    #with open(data_path, 'wb') as f:
    #    pickle.dump(lists, f)

    with open(data_path, 'rb') as f:
        lists = pickle.load(f)

    for i in range(len(lists)):
        start_time = perf_counter()
        quicksort(lists[i], 0, size-1)
        #lists[i].sort()
        end_time = perf_counter()
        elapsed_time = end_time - start_time

        print(f'list {i:2}, num of repeat elements: {10**5 * i:7}, ' \
                f'execution time: {elapsed_time:.3f} s')

    '''#validate the correctness
    array1 = lists[0].copy()
    array2 = lists[0].copy()
    array1.sort()
    quicksort(array2, 0, size-1)
    print(array1 == array2)'''
