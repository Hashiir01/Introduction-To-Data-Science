feedback = {
    1: {'rating': 5, 'comments': 'Excellent service'},
    2: {'rating': 4, 'comments': 'Very good experience'},
    3: {'rating': 3, 'comments': 'Okay'},
    4: {'rating': 2, 'comments': 'Not great'},
    5: {'rating': 4, 'comments': 'Good overall'},
    6: {'rating': 5, 'comments': 'Loved it!'},
}

def high_rating(d):
    for id,detail in d.items():
        if detail['rating']>=4:
            print(id,detail)

def sorrt(d,n):
    s=sorted(d.items(),key=lambda item:item[1]['rating'],reverse=True)
    s1=s[:n]
    print(f'{s}\n\n\n{s1}')


def combine(d1,d2):
    comb= {}
    
    for id, d in d1.items():
        comb[id] = {
            'rating': d['rating'],
            'comments': [d['comments']]}
    
    for id, d in d2.items():
        if id in comb:
            comb[id]['rating'] = max(comb[id]['rating'], d['rating'])
            comb[id]['comments'].append(d['comments'])
        else:
            comb[id] = {
                'rating': d['rating'],
                'comments': [d['comments']]}
    return comb

    


