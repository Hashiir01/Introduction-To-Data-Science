l=[
    (1,"hashir",50,"pakistan"),
    (2,"qaiser",23,"Canada"),
    (3,"subhan",25,"pakistan"),
    (4,"fawad",22,"Canada"),
    (5,"bilal",10,"USA"),
    (6,"raqeeb",32,"USA"),
    (6,"salman",34,"USA"),
    (6,"ali",32,"USA"),
    (6,"ali",12,"USA"),
    (6,"ali",23,"USA"),
    (6,"ali",10,"USA"),
    (6,"ali",38,"USA")
]

def filter (list):
    len1=len(list)
    list1=[]
    for i in range (len1):
        if list[i][2] > 30:
            if list[i][3]=='USA' or list[i][3]=='Canada':
                list1.append(list[i])
    return list1

def sorrt(list):
    old=[]
    sort_l=sorted(list,key=lambda x:x[2])
    l=len(sort_l)
    for i in range(8):
        old.append(sort_l[-1])
        sort_l.pop()
    return old



print(sorrt(l))

