In [4]:
dfa =   {
        'a':{0:'a',1:'b'},
        'b':{0:'a',1:'c'},
        'c':{0:'a',1:'d'},
        'd':{0:'d',1:'a'},
        }


def mydfa(r):
    s = str(r)
    ins = 'a'
    fis = ['d']
    for i in s:
        ins = dfa[ins][int(i)]
    if ins in fis:
        return True
    else:
        return False

mydfa('0100111100111')
Out[4]:
True