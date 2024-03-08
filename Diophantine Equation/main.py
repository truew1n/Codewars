def sol_equa(n):
    res = []
    Factors = [1]
    i = 2
    while i <= n**(1/2):
        if n % i == 0:
            Factors.append(i)
        i += 1
    W = 4
    for x in Factors:
        a1, a2 = x, int(n/x)
        Wx, Wy = (a1*2) - (a2*-2), (1*a2) - (1*a1) 
        if (Wx/W >= 0 and Wx/W == int(Wx/W)) and (Wy/W >= 0 and Wy/W == int(Wy/W)):
            res.append([int(Wx/W), int(Wy/W)])
    return res
