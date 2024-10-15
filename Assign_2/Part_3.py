A={1,2,3,4}
B={1,2,7,5}
C={2,3,4,5}

def finnd(A,B):
    Q={''}
    W={''}
    for i in A:
        for j in B:
            if i==j:
                Q.add(i)
    
    for i in A:
        for j in B:
            if i in B:
                break
            W.add(i)
    for i in B:
        for j in A:
            if i in A:
                break
            W.add(i)
            
    # for i in A:
    #     for j in C:
    #         if j!=i:
    #             W.add(j)
    return Q,W

def update(A,id):
    A.add(id)

def remove(A,id):
    A.remove(id)


