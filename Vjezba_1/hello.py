print("Hello world!")

petlja=True
while petlja == True:
    x1=(input("Unesite prvi broj: "))
    y1=(input("Unesite drugi broj: "))
    x2=(input("Unesite treći broj: "))
    y2=(input("Unesite četvrti broj: "))

    if x1.isnumeric()==True and x2.isnumeric()==True and y1.isnumeric()==True and y2.isnumeric()==True:
        petlja=False
    else:
        print("Vrijednost nije broj.")
k=(int(y2)-int(y1))/(int(x2)-int(x1))
l=(int(y1)-int(k)*int(x1))
print('Formula pravca je: y=',k, '*x+', l) 
    
    

