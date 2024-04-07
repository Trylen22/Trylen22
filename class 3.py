N = 74754 # the decimal number
b = 16 # the desired base system
Q = [] # an empty list that will contain the quotients
R = [] # an empty list that will contain the remainders

i = 0
Q.append(N//b)
R.append(N%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

print(Q)
print(R)
