l=[
    (1,12,200,''),
    (2,11,2000,''),
    (3,11,2002,''),
    (4,12,20022,''),
    (5,13,20012,''),
    (6,14,2043,''),
    (7,15,20056,''),
    (8,11,30000,''),
]

def unique(list):
    u=[]
    for i in range (len(list)):
        if list[i][1] not in u:
            u.append(list[i][1])
    return u

def maxx(list):
    s= max(list,key=lambda x:x[2])
    return s

def lists(list):
    t_id=[]
    u_id=[]
    for i in range (len(list)):
        u_id.append(list[i][0])
        t_id.append(list[i][1])
    return f'Transactions ID:{t_id}\nUser ID:{u_id}'

