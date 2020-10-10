A1 = [1,4,9]
A2 = [9,9,9]

def plus_one(A):
    A[-1] += 1
    for i in range(1,len(A))[::-1]:
        if A[i] != 10:
            break
        else:
            A[i] = 0
            A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

print(plus_one(A2))

#s = ''.join(map(str, A))
