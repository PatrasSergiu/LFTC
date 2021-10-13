def extend(a):
    out = []
    for sublist in a:
        out.extend(sublist)
    return out
for file in range(1,5):
    initial = []
    with open('ex' + str(file) + '.txt', 'r') as f:
        for x in f:
            initial.append(x.strip())

    initial = list(filter(None, initial))
    separators = ['(', ')', '{', '}', ';', '<', '>', ',']
    space = ' '
    separators = separators + list(space)
    mid = []
    for x in initial:
        x = x.split();
        mid.append(x)

    mid = extend(mid)

    final = []
    for x in mid:
        hasSeparator = 0;
        for s in separators:
            if s in x:
                hasSeparator = 1;
                index = x.find(s)
                final.append(x[:index]);
                #pentru cazuri gen +=, trebuie o verificare gen if x[index+1] e separator, atunci continue
                final.append(s);
                final.append(x[index+1:])
        if(hasSeparator == 0):
            final.append(x)

    final = list(filter(None, final))

    with open('output' + str(file) + '.txt', 'w') as f:
        for el in final:
            f.write(el + '\n')
