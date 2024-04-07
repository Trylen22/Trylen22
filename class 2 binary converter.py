def dec_to_base(N,b):
    Q= []
    R= []

    Q.append(N // b)
    R.append(N % b)


    while Q[-1] !=0:
        R.append(Q[-1] % b)
        Q.append(Q[-1]// b)
        

        R.reverse()

    S = " "

    for digit in R:
        S += (str(digit)) 

    return S

print(dec_to_base(74754, 16))