#adding name to the list until user gives end
l=[]
while len(l)==0 or len(l)!=0:
    n=input('name=')
    if n not in l:
        l.append(n)
        if n=='end':
            l.remove('end')
            break
    if n in l:
        continue
print('list of names:', l)
