def teams(candidates, k):
    if k == 0:
        return []

    print(combinacoes(candidates, k))
    return teams(candidates, k - 1)


def combinacoes(candidates, n):
    if(n == 1):
        generated = []
        for i in range(0, len(candidates)):
            temp = [candidates[i]]
            generated.append(temp)
        return generated

    generated = []
    for i in range(0, len(candidates)):
        candidates_cpy = candidates.copy()
        temp = [candidates_cpy.pop(i)]
        j = 0
        for j in range(0, (n - 1)):
            temp.append(candidates_cpy[j])
        generated.append(temp)
        temp = [candidates.copy().pop(i)]
        while(j >= 0):
            temp.append(candidates_cpy[j])
            j -= 1
        generated.append(temp)
        
    return generated
    
teams(['a', 'b', 'c'], 3)
