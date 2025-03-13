import matplotlib.pyplot as plt
def funkcija(x1, x2, y1, y2,option='Graph'):
    if isinstance(x1,int) and isinstance(x2,int) and isinstance(y1,int) and isinstance(y2,int):
        k=(y2-y1)/(x2-x1)
        l=(y1-k*x1)
        print('Formula pravca je: y=',k, '*x+', l) 
        x=[x1, x2]
        y=[y1, y2]
        plt.plot(x,y)
        if option=='Graph':
            plt.show()
        else:
            plt.savefig(option)
funkcija(3, 4, 8, 9,"Željko")       