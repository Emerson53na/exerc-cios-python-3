 ' => ', end='')
    
    if go < n:
        seq1 = seq1 + seq2
        print(f'{seq2}', end='')
        
    go += 1
    if go < n:
        print(' => ', end='')
