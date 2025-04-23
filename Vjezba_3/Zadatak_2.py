def broj_iteracija(N):
    x = 5
    for i in range(0,N):
        x += 1/3
    for i in range(0, N):
        x-=1/3
    return(x)
broj_iteracija(200)
broj_iteracija(2000)
broj_iteracija(20000)
