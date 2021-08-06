def distance(strand_a, strand_b):
    la = len(strand_a)
    lb = len(strand_b)
    if la != lb :
        raise ValueError('Not Equal')
    
    else :
        counter = 0
        for i in range(la):
            if strand_a[i] != strand_b[i]:
                counter += 1
    return counter
    
